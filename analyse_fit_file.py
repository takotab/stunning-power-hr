import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fitparse import FitFile
import seaborn as sns
import json
from scipy import signal
from scipy import stats

import utils


def fill_na(result, i):
    for key in result.keys():
        if i not in result[key]:
            result[key][i] = 0
    return result


def get_index(df, time=60, power=175):
    rolling_power = df.power.rolling(time).mean()
    a = np.abs(rolling_power - np.ones_like(rolling_power.array))
    argmin = np.argmin(a)
    print(argmin)
    return argmin


def get_joule(power):
    return power.sum()


def plot_file(file):
    print(utils.get_name(file))
    result = {}
    fitfile = FitFile(file)

    # Get all data messages that are of type record
    for i, record in enumerate(fitfile.get_messages("record")):
        # Go through all the data entries in this record
        for record_data in record:
            if not str(record_data.name) in list(result.keys()):
                result[str(record_data.name)] = {}

            result[record_data.name][i] = record_data.value
        result = fill_na(result, i)

    df = pd.DataFrame().from_dict(result)
    fig = plt.figure(figsize=(20, 20))
    df.loc[:, ["cadence", "power", "heart_rate"]].plot()

    df.to_csv(file.replace(".fit", ".csv"))
    info = utils.get_info(file)

    start = int(info["start(sec)"])
    end = int(info["end(sec)"])

    fig = plt.figure(figsize=(16, 16))  # Create matplotlib figure

    ax = fig.add_subplot(111)  # Create matplotlib axes
    ax2 = ax.twinx()  # Create another axes that shares the same x-axis as ax.
    df.loc[start:end, ["power"]].plot(color="purple", ax=ax)
    patches, labels = ax.get_legend_handles_labels()

    ax.legend(patches, labels, loc="upper left")
    df.loc[start:end, ["heart_rate"]].plot(color="red", ax=ax2)
    df.loc[start:end, ["cadence"]].plot(color="blue", ax=ax2)

    ax.set_ylabel("Power (W)")
    ax2.set_ylabel("Heart rate / Cadance (Bpm)")
    ax.set_xlabel("Tijd (sec)")

    plt.show()
    fig.savefig(file.replace(".fit", "_plot.png"), dpi=fig.dpi)

    info["total work (J)"] = str(df.loc[start:end, "power"].array.sum())
    info["Max hartslag (bpm)"] = np.round(
        (df.loc[start : end + 30, "heart_rate"].rolling(30).mean().max()), 2
    )
    info["Max power (W)"] = np.round(
        df.loc[start : end + 30, "power"].rolling(30).mean().max(), 2
    )
    f_overall = os.path.join("data", "totaal", "overall.json")
    if not info["gewicht(kg)"] == "Onbekend" and os.path.isfile(f_overall):
        total = json.load(open(f_overall, "r"))
        name = utils.get_name(file)
        value = np.round(info["Max power (W)"] / float(info["gewicht(kg)"]), 2)
        info["Max power per kg (W/kg)"] = value
        if utils.get_name(file) in total:
            if type(total[name]) == str:
                total[name] = [total[name], value]
            elif type(total[name]) == list:
                total[name].append(value)
        else:
            total[name] = [value]
        json.dump(total, open(f_overall, "w"))

    info["hr-zones"] = {}
    info["hr-zones"]["Herstel training (H)"] = [
        info["Max hartslag (bpm)"] * 0.50,
        info["Max hartslag (bpm)"] * 0.65,
    ]
    info["hr-zones"]["Extensieve duurtraining (D1)"] = [
        info["Max hartslag (bpm)"] * 0.65,
        info["Max hartslag (bpm)"] * 0.75,
    ]
    info["hr-zones"]["Intensieve duurtraining (D2)"] = [
        info["Max hartslag (bpm)"] * 0.75,
        info["Max hartslag (bpm)"] * 0.85,
    ]
    info["hr-zones"]["Extensieve herhalingen (D3)"] = [
        info["Max hartslag (bpm)"] * 0.85,
        info["Max hartslag (bpm)"] * 0.95,
    ]
    info["hr-zones"]["Intensieve herh/interval (HIIT)"] = [
        info["Max hartslag (bpm)"] * 0.95,
        info["Max hartslag (bpm)"] * 1,
    ]

    for key, item in info["hr-zones"].items():
        info["hr-zones"][key] = (int(item[0]), int(item[1]))

    utils.set_info(file, info)

    print(info)


if __name__ == "__main__":

    total = {}
    utils.apply_to_fitfile(plot_file, all=True)

