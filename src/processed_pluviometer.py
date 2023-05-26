import os
from plot_paths import *
from pluviometer_plot import *

if __name__ == "__main__":
    files = os.listdir(CLASSIFIED_PLUVIOMETER_PATH)
    pluviometer_plot(CLASSIFIED_PLUVIOMETER_PATH, "./img/graphics/processed_data/")
