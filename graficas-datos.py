import matplotlib.pyplot as plt
import pandas as pd

RAW_FILES_PATH = './data/classified_data/'
FILES = ["sensor1.csv", "sensor2.csv", "sensor3.csv", "sensor4.csv", "sensor5.csv", "sensor6.csv", "sensor7.csv", "sensor8.csv"]

def main():
    sensor_graphic()

def sensor_graphic():

    file_counter = 1
    for file in FILES:
        dataset = pd.read_csv(RAW_FILES_PATH + file)

        x = dataset["ts"]

        ts_final = max(x)
        ts_inicial = min(x)

        plt.figure(num = "Graficas " + file, figsize=(15, 7.5))
        plt.suptitle("Graficas del sensor " + str(file_counter))

        # plt.subplot(4, 2, 1)
        # plt.scatter(x, dataset["bateria"], marker=".", linewidths=0.1, s=0.5)
        # plt.grid(True)
        # plt.xlim(ts_inicial, ts_final)
        # plt.ylabel("Batería")
        
        # plt.subplot(4, 2, 2)
        # plt.scatter(x, dataset["bateria"], marker=".", linewidths=0.1, s=0.5)
        # plt.grid(True)
        # plt.xlim(ts_inicial, ts_final)
        # plt.ylabel("Batería")

        plt.subplot(3, 2, 1)
        plt.scatter(x, dataset["t_ext"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.xlim(ts_inicial, ts_final)
        plt.ylabel("Temp Ext")

        plt.subplot(3, 2, 2)
        plt.scatter(x, dataset["h_ext"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.xlim(ts_inicial, ts_final)
        plt.ylabel("Humedad Ext")

        plt.subplot(3, 2, 3)
        plt.scatter(x, dataset["t_C_cal"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.xlim(ts_inicial, ts_final)
        plt.ylabel("Temp Corta")

        plt.subplot(3, 2, 4)
        plt.scatter(x, dataset["h_C_cal"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.xlim(ts_inicial, ts_final)
        plt.ylabel("Humedad Corta")

        plt.subplot(3, 2, 5)
        plt.scatter(x, dataset["t_L_cal"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        plt.xlim(ts_inicial, ts_final)
        plt.ylabel("Temp Larga")

        plt.subplot(3, 2, 6)
        plt.scatter(x, dataset["h_L_cal"], marker=".", linewidths=0.1, s=0.5)
        plt.grid(True)
        # if file_counter == 1:
        #     plt.ylim(bottom = 0, top = 50)
        plt.xlim(ts_inicial, ts_final)
        plt.ylabel("Humedad Larga")

        plt.savefig(fname = "./img/graphics/sensor" + str(file_counter))

        # plt.figure(num = "Graficas de humedad no calibradas", figsize=(15, 7.5))
        # plt.suptitle("Graficas de humedad del sensor " + str(file_counter))
        
        # plt.subplot(3, 1, 1)
        # plt.plot(x, dataset["bateria"], '-')
        # plt.grid(True)
        # plt.xlim(ts_inicial, ts_final)
        # plt.ylabel("Batería")

        # plt.subplot(3, 1, 2)
        # dataset["h_C"].loc[dataset["h_C"] > 20000] = None
        # min_h, max_h = dataset["h_C"].min(), dataset["h_C"].max()
        # plt.plot(x, dataset["h_C"], 'g-')
        # plt.grid(True)
        # plt.xlim(ts_inicial, ts_final)
        # plt.ylim(min_h, max_h)
        # plt.ylabel("Humedad C. no calibrada")
        
        # plt.subplot(3, 1, 3)
        # dataset["h_L"].loc[dataset["h_L"] > 20000] = None
        # min_h, max_h = dataset["h_L"].min(), dataset["h_L"].max()
        # plt.plot(x, dataset["h_L"], 'r-')
        # plt.grid(True)
        # plt.xlim(ts_inicial, ts_final)
        # plt.ylim(min_h, max_h)
        # plt.ylabel("Humedad L. no calibrada")

        # plt.savefig(fname = "./img/graphics/humedadSensor" + str(file_counter))

        file_counter += 1

        plt.show()


if __name__ == "__main__":
    main()