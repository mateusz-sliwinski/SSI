import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import zad1


class Visualization:
    def show_iris_stats(self):
        dataset = zad1.DecisionSystem('data/iris.txt', 'data/iris-type.txt')
        dataset.objects = dataset.get_all_objects()
        data = dataset.objects
        datasets = []

        for i in range(len(data)):
            df = pd.DataFrame(data[i], columns=["0", "1", "2", "3", "4"]).astype(float)
            datasets.append(df)

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].plot(datasets[0]["3"], datasets[0]["4"], 'o', c='y', label="Setosa")
        axs[0, 0].plot(datasets[1]["3"], datasets[1]["4"], 'o', c='b', label="Versicolour")
        axs[0, 0].plot(datasets[2]["3"], datasets[2]["4"], 'o', c='r', label="Virginica")
        axs[0, 0].set_title('Plot 1')
        axs[0, 0].set_xlabel("Petal length")
        axs[0, 0].set_ylabel("Petal width")

        axs[0, 1].plot(datasets[0]["2"], datasets[0]["4"], 'o', c='y', label="Setosa")
        axs[0, 1].plot(datasets[1]["2"], datasets[1]["4"], 'o', c='b', label="Versicolour")
        axs[0, 1].plot(datasets[2]["2"], datasets[2]["4"], 'o', c='r', label="Virginica")
        axs[0, 1].set_title('Plot 2')
        axs[0, 1].set_xlabel("Sepal width")
        axs[0, 1].set_ylabel("Petal width")

        axs[1, 0].plot(datasets[0]["1"], datasets[0]["4"], 'o', c='y', label="Setosa")
        axs[1, 0].plot(datasets[1]["1"], datasets[1]["4"], 'o', c='b', label="Versicolour")
        axs[1, 0].plot(datasets[2]["1"], datasets[2]["4"], 'o', c='r', label="Virginica")
        axs[1, 0].set_title('Plot 3')
        axs[1, 0].set_xlabel("Sepal length")
        axs[1, 0].set_ylabel("Petal width")

        axs[1, 1].plot(datasets[0]["2"], datasets[0]["3"], 'o', c='y', label="Setosa")
        axs[1, 1].plot(datasets[1]["2"], datasets[1]["3"], 'o', c='b', label="Versicolour")
        axs[1, 1].plot(datasets[2]["2"], datasets[2]["3"], 'o', c='r', label="Virginica")
        axs[1, 1].set_title('Plot 4')
        axs[1, 1].set_xlabel("Sepal width")
        axs[1, 1].set_ylabel("Petal length")

        plt.legend()

        fig.tight_layout(pad=1)
        plt.show()


a = Visualization()
a.show_iris_stats()
