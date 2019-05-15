import utils
import os


def add_weight(file):
    filename = os.path.join(*file.split(os.sep)[:-1]) + "/info.txt"
    if os.path.isfile(filename):
        return
    kg = input("wat is het gewicht van " + file + " ? ")
    if str(kg) == "0":
        kg = "Onbekend"
    with open(filename, "w") as f:
        f.write("gewicht(kg):" + kg)


if __name__ == "__main__":
    utils.apply_to_fitfile(add_weight, all=True)

