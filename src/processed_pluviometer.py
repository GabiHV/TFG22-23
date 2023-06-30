import os
from env_paths import *
from pluviometer_plot import *

if __name__ == "__main__":
    files = os.listdir(CLASSIFIED_PLUVIOMETER_PATH)
    
    # Etiquetas de las graficas de la figura
    LABELS = {"pluv_deltaMM" : "litros/m^2"}

    pluviometer_plot(CLASSIFIED_PLUVIOMETER_PATH, "../img/graphics/processed_data/", LABELS, (1, 1))
