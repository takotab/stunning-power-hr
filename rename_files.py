import matplotlib.pyplot as plt
import os
import glob
from fitparse import FitFile


import pandas as pd

# from fit import FitFile
# from fit.files.activity import ActivityFile
# from fit.messages.common import FileCreator


def rename():
    for file in glob.glob("data/vu*/*/*/*.fit"):
        print(file)
        fitfile = FitFile(file)

        # Get all data messages that are of type record
        for record in fitfile.get_messages("record"):
            result = {}
            # Go through all the data entries in this record
            for record_data in record:
                if not record_data.name in result:
                    result[record_data.name] = []
                result[record_data.name].append(record_data.value)
        df = pd.DataFrame().from_dict(result)
        df.plot()
        plt.show()


if __name__ == "__main__":
    rename()
