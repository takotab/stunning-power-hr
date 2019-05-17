import json

import utils


def txt2json(file):
    result = {}
    with open(file, "r") as f:
        for line in f:
            key, value = line.split(":")
            result[key] = value.replace("\n", "")

    json.dump(result, open(file.replace(".txt", ".json"), "w"))


if __name__ == "__main__":
    utils.apply_to_fitfile(txt2json, filetype="txt", all=True)

