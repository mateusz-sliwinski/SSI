import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

import zad1


class Visualization:
    def show_iris_stats(self):
        data = zad1.DecisionSystem('data/iris.txt', 'data/iris-type.txt')
        take_data = data.get_all_object_float([_ for _ in range(0, 150)], [_ for _ in range(0, 5)])

        datasets = []
        df = pd.DataFrame(take_data)
        df.columns = ['1', '2', '3', '4', 'Decision']
        datasets.append(df)

        fig, axs = plt.subplots(2, 2)
        for counter in range(len(df)):
            if df["Decision"][counter] == 1:
                axs[0, 0].plot(df["3"][counter], df["4"][counter], 'o', c='y', label="Setosa")
            if df["Decision"][counter] == 2:
                axs[0, 0].plot(df["3"][counter], df["4"][counter], 'o', c='b', label="Versicolour")
            if df["Decision"][counter] == 3:
                axs[0, 0].plot(df["3"][counter], df["4"][counter], 'o', c='r', label="Virginica")

            if df["Decision"][counter] == 1:
                axs[0, 1].plot(df["2"][counter], df["4"][counter], 'o', c='y', label="Setosa")
            if df["Decision"][counter] == 2:
                axs[0, 1].plot(df["2"][counter], df["4"][counter], 'o', c='b', label="Versicolour")
            if df["Decision"][counter] == 3:
                axs[0, 1].plot(df["2"][counter], df["4"][counter], 'o', c='r', label="Virginica")

            if df["Decision"][counter] == 1:
                axs[1, 0].plot(df["1"][counter], df["4"][counter], 'o', c='y', label="Setosa")
            if df["Decision"][counter] == 2:
                axs[1, 0].plot(df["1"][counter], df["4"][counter], 'o', c='b', label="Versicolour")
            if df["Decision"][counter] == 3:
                axs[1, 0].plot(df["1"][counter], df["4"][counter], 'o', c='r', label="Virginica")

            if df["Decision"][counter] == 1:
                axs[1, 1].plot(df["2"][counter], df["3"][counter], 'o', c='y', label="Setosa")
            if df["Decision"][counter] == 2:
                axs[1, 1].plot(df["2"][counter], df["3"][counter], 'o', c='b', label="Versicolour")
            if df["Decision"][counter] == 3:
                axs[1, 1].plot(df["2"][counter], df["3"][counter], 'o', c='r', label="Virginica")

        axs[1, 1].set_title('Plot 4')
        axs[1, 1].set_xlabel("Sepal width")
        axs[1, 1].set_ylabel("Petal length")

        axs[0, 0].set_title('Plot 1')
        axs[0, 0].set_xlabel("Petal length")
        axs[0, 0].set_ylabel("Petal width")

        axs[0, 1].set_title('Plot 2')
        axs[0, 1].set_xlabel("Sepal width")
        axs[0, 1].set_ylabel("Petal width")

        axs[1, 0].set_title('Plot 3')
        axs[1, 0].set_xlabel("Sepal length")
        axs[1, 0].set_ylabel("Petal width")

        setosa_patch = mpatches.Patch(color='yellow', label='Setosa')
        versicolour_patch = mpatches.Patch(color='blue', label='Versicolour')
        virginica_patch = mpatches.Patch(color='red', label='Virginica')

        plt.legend(handles=[setosa_patch, versicolour_patch, virginica_patch], loc=0, prop={'size': 7.5})

        plt.show()


a = Visualization()
a.show_iris_stats()
