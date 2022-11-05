import random
from math import sin
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')


def evolutionary_algorithm(spread, growth_rate, iteration, range_variability):
    x = random.choice([_ for _ in range(0, range_variability)])
    y = sin(x / 10) * sin(x / 200)
    list_x, list_y = [], []

    for main in range(iteration):
        x_pot = x + random.uniform(-spread, spread)

        while x_pot > 100 or x_pot < 0:
            x_pot = x + random.uniform(-spread, spread)

        y_pot = sin(x_pot / 10) * sin(x_pot / 200)

        if y_pot > y:
            x = x_pot
            y = y_pot
            spread *= growth_rate
        else:
            spread /= growth_rate

        print(f'Iteration {main} x: {x} y:{y} spread: {spread}')

        list_y.append(y)
        list_x.append(x)

        x_main_plot = np.arange(0, 100, 1)
        y_main_plot = np.sin(x_main_plot / 10) * np.sin(x_main_plot / 200)
        plt.plot(x_main_plot, y_main_plot)
        plt.plot(x, y, 'o', color='red', label="Point")
        plt.show()


evolutionary_algorithm(10, 1.1, 100, 100)
