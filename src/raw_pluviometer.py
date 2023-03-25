import os
from env_paths import *
from pluviometer_plot import *

if __name__ == "__main__":
    files = [file for file in os.listdir(PLUVIOMETER_FILES_DIRECTORY) if ".csv" in file]

    pluviometer_plot(PLUVIOMETER_FILES_DIRECTORY)
