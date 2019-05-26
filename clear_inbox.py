from glob import glob
import os
from fitparse import FitFile
import json

from add_weight import add_weight
from start_end import get_start_end
from analyse_fit_file import plot_file
from make_pdf import make_pdf
from gender import gender


def clear_inbox():
    for file in glob("data/inbox/*.fit"):
        name = name_file(file)
        if not os.path.isdir("data/" + os.sep + name):
            os.mkdir("data/" + name)
        date = date_file(file).strftime("%Y-%m-%d")
        folder = os.path.join("data", name, date)
        if not os.path.isdir(folder):
            os.mkdir(folder)
        new_filename = os.path.join(folder, name + "-" + date + ".test_file.fit")
        os.rename(file, new_filename)
        json.dump({}, open(os.path.join(folder, "info.json"), "w"))
        print("info made for " + name)
        add_weight(new_filename)
        get_start_end(new_filename)
        gender(new_filename)
        plot_file(new_filename)
        make_pdf(new_filename)


def name_file(file: str):
    name = input("Van wie is deze file " + file + " ?").lower()
    return name[0].upper() + name[1:]


def date_file(file: str):
    fitfile = FitFile(file)
    # Get all data messages that are of type record
    for record in fitfile.get_messages("record"):
        for record_data in record:
            if record_data.name == "timestamp":
                print(record_data)
                return record_data.value
        break


if __name__ == "__main__":
    clear_inbox()
