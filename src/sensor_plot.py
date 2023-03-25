import matplotlib.pyplot as plt
import pandas as pd

# Etiquetas de las graficas de la figura
LABELS = {"t_ext" : "Temp Ext", "h_ext" : "Humedad Ext", "t_C_cal" : "Temp Corta", "h_C_cal" : "Huemdad Corta", "t_L_cal" : "Temp Larga", "h_L_cal" : "Humedad Larga"}

def sensor_plot(files, path):

    for file_counter, file in enumerate(files, start=1):
        dataset = pd.read_csv(path + file)

        x = dataset["ts"]

        ts_final = max(x)
        ts_inicial = min(x)

        plt.figure(num = "Graficas " + file, figsize=(15, 7.5))
        plt.suptitle("Graficas del sensor " + str(file_counter))

        # Por cada etiqueta habra una grafica correspondiente con la columna X del DataFrame
        for pos, key in enumerate(LABELS, start=1):
            plt.subplot(3, 2, pos)
            plt.scatter(x, dataset[key], marker=".", linewidths=0.1, s=0.5)
            plt.grid(True)
            plt.xlim(ts_inicial, ts_final)
            plt.ylabel(LABELS[key])

        plt.show()