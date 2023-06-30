import pandas as pd
import matplotlib.pyplot as plt

def pluviometer_plot(path, save_path, labels, subplot_size):
    dataset = pd.read_csv(path + "pluviometro.csv")

    fig = plt.figure(num="Graficas del pluviometro", figsize=(15, 7.5))
    plt.suptitle("Graficas del pluviometro")

    # Por cada etiqueta habra una grafica correspondiente con la columna X del DataFrame
    for pos, key in enumerate(labels, start=1):
        plt.subplot(subplot_size[0], subplot_size[1], pos)
        plt.scatter(dataset["ts"], dataset[key], marker=".", linewidths=0.5, s=0.5)
        plt.grid(True)
        plt.ylabel(labels[key])
    
    plt.show()

    fig.savefig(save_path + 'pluviometro.png')