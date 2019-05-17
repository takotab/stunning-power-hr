import os
import numpy as np

from vu_test_power_profile import Person
from utils import (
    apply_to_fitfile,
    get_json,
    get_name,
    get_info,
    get_date,
    get_file,
    set_info,
)
from make_pdf import make_pdf


def test_utils_get_json():
    def check(file):
        json = get_json(file)
        assert json.split(".")[-1] == "json"
        assert get_date(json) == get_date(file)
        assert get_name(json) == get_name(file)

    apply_to_fitfile(check)


def test_set_info():
    file = next(get_file(name="Eric", unit_test=True))
    info = get_info(file)
    new_info = str(np.random.rand())
    info["test"] = new_info
    set_info(file, info)
    cur_info = get_info(file)
    assert cur_info["test"] == new_info


def test_pdf():
    file = next(get_file(name="Eric", unit_test=True))
    make_pdf(file)
    assert os.path.isfile(file.replace("fit", "pdf"))


if __name__ == "__main__":
    froome = Person(375, 20250)
    current_p = 150
    done = True
    while done:
        done = froome.cycle(current_p, 60)
        current_p += 25
        if current_p > 900:
            break
