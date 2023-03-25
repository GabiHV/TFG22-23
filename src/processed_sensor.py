import os
from env_paths import *
from sensor_plot import *

if __name__ == "__main__":
    files = os.listdir(CLASSIFIED_SENSOR_PATH)

    sensor_plot(files, CLASSIFIED_SENSOR_PATH)
