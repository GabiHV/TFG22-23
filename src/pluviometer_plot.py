import pandas as pd
import matplotlib.pyplot as plt

# Etiquetas de las graficas de la figura
LABELS = {"pluv" : "Balancin", "pluv_delta" : "Pluv_actual - Pluv_anterior", "pluv_deltaMM" : "litros/m^2"}

def pluviometer_plot(path, save_path):
    dataset = pd.read_csv(path + "pluviometro.csv")

    fig = plt.figure(num="Graficas del pluviometro", figsize=(15, 7.5))
    plt.suptitle("Graficas del pluviometro")

    # Por cada etiqueta habra una grafica correspondiente con la columna X del DataFrame
    for pos, key in enumerate(LABELS, start=1):
        plt.subplot(2, 2, pos)
        plt.scatter(dataset["ts"], dataset[key], marker=".", linewidths=0.5, s=0.5)
        plt.grid(True)
        plt.ylabel(LABELS[key])
    
    plt.show()

    fig.savefig(save_path + 'pluviometro.png')