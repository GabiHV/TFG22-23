import os
from env_paths import *
from pluviometer_plot import *

if __name__ == "__main__":
    files = os.listdir(CLASSIFIED_PLUVIOMETER_PATH)
    pluviometer_plot(CLASSIFIED_PLUVIOMETER_PATH)
