import matplotlib.pyplot as plt
import pandas as pd

RAW_FILES_PATH = './data/raw_data/'
FILES = ["pluviometro.csv"]

def main():
    pluviometer_graphic()

def pluviometer_graphic():

    for file in FILES:
        dataset = pd.read_csv(RAW_FILES_PATH + file)

        plt.figure(num = "Graficas pluviometro", figsize=(15, 7.5))
        plt.suptitle("Graficas del pluviometro")

        x = dataset["ts"]
        plt.subplot(2, 2, 1)
        plt.scatter(x, dataset["bateria"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.ylabel("Batería")

        plt.subplot(2, 2, 2)
        plt.scatter(x, dataset["pluv"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.ylabel("Pluv")

        plt.subplot(2, 2, 3)
        plt.scatter(x, dataset["pluv_delta"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.ylabel("Pluv_Delta")

        plt.subplot(2, 2, 4)
        plt.scatter(x, dataset["pluv_deltaMM"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.ylabel("Pluv_Delta MM")

        plt.savefig(fname = "./img/graphics/pluviometro")

        plt.show()

if __name__ == "__main__":
    main()
