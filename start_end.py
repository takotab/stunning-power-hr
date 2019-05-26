import pandas as pd
from fitparse import FitFile
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

import utils


def fill_na(result, i):
    for key in result.keys():
        if i not in result[key]:
            result[key][i] = 0
    return result


def get_start_end(file):
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
    good = False
    while not good:
        ax = df.loc[:, ["cadence", "power", "heart_rate"]].plot()
        plt.show()
        start = int(input("start? "))
        end = int(input("end? "))
        ax = df.loc[start:end, ["cadence", "power", "heart_rate"]].plot()
        plt.show()
        good = input("good? (y/n) ") == "y"
    info = utils.get_info(file)
    info["start(sec)"] = str(start)
    info["end(sec)"] = str(end)
    utils.set_info(file, info)
    df.to_csv(file.replace(".fit", ".csv"))
    sns.lmplot(x="power", y="heart_rate", data=df)


if __name__ == "__main__":
    utils.apply_to_fitfile(plot_file, all=True)
