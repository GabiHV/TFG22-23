import os
from env_paths import *
from sensor_plot import *

if __name__ == "__main__":
    files = os.listdir(SENSOR_FILES_DIRECTORY)

    sensor_plot(files, SENSOR_FILES_DIRECTORY)