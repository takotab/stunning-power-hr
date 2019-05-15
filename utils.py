import os
import glob


def apply_to_fitfile(fnc, name: str = "*", date="*", filetype="fit", all=False):
    for file in glob.glob("data/" + name + "/" + date + "/*." + filetype):
        fnc(file)
        print("excecuted on " + get_name(file))
        if not all:
            break


def get_name(file):
    return file.split(os.sep)[-3]

