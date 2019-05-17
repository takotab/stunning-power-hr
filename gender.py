import utils


def gender(file):
    info = utils.get_info(file)
    while "sex" not in info:
        sex = input("what is the sex of " + utils.get_name(file) + "? (m/w) ")
        if sex == "m" or sex == "w":
            info["sex"] = sex
        else:
            print("please enter m or w ")
    utils.set_info(file, info)


if __name__ == "__main__":
    utils.apply_to_fitfile(gender, all=True)
