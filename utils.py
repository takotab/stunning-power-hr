import os
import glob
import json
import numpy as np


def apply_to_fitfile(fnc, name: str = "*", date="*", filetype="fit", all=False):
    for file in get_file(name=name, date=date, filetype=filetype):
        fnc(file)
        print("excecuted on " + get_name(file))
        if not all:
            break


def get_file(name: str = "*", date="*", filetype="fit", unit_test=False):
    DATA_DIR = "data"
    if unit_test:
        DATA_DIR = "fake_data"
    for file in glob.glob(DATA_DIR + "/" + name + "/" + date + "/*" + filetype):
        yield file


def get_name(file):
    return file.split(os.sep)[-3]


def get_date(file):
    return file.split(os.sep)[-2]


def get_json(file):
    for file in get_file(name=get_name(file), date=get_date(file), filetype=".json"):
        return file
    return None


def get_info(file):
    info = get_json(file)
    if info is None:
        FileExistsError(file + " .json")
    return json.load(open(info, "r"))


def set_info(file: str, info: dict):
    result = {}
    for key, item in info.items():
        result[key] = item

    json.dump(result, open(get_json(file), "w"))

