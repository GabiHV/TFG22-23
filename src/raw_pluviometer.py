import os
from env_paths import *
from pluviometer_plot import *

if __name__ == "__main__":
    files = [file for file in os.listdir(PLUVIOMETER_FILES_DIRECTORY) if ".csv" in file]
    
    # Etiquetas de las graficas de la figura
    LABELS = {"pluv" : "Balancin", "pluv_delta" : "Pluv_actual - Pluv_anterior", "pluv_deltaMM" : "litros/m^2"} 

    pluviometer_plot(PLUVIOMETER_FILES_DIRECTORY, "../img/graphics/raw_data/", LABELS, (2, 2))
