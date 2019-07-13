import utils
import os
import json


def add_weight(file):
    info = utils.get_info(file)
    kg = input("wat is het gewicht van " + utils.get_name(file) + " ? ")

    if str(kg) == "0":
        kg = "Onbekend"
    info["gewicht(kg)"] = kg
    utils.set_info(file, info)


if __name__ == "__main__":
    utils.apply_to_fitfile(add_weight, date="2019-07-06", all=True)

