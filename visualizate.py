import matplotlib.pyplot
import numpy as np
from matplotlib import pyplot as plt


def clean_plot() -> None:
    matplotlib.pyplot.cla()


def draw_dashed_plot(x_cos: list[float], y_curved: list[float]) -> None:
    start_elipse = np.linspace(x_cos[0], x_cos[1] * np.pi, y_curved[0])
    cos_x = x_cos[1] * np.cos(start_elipse)
    sin_y = x_cos[1] * np.sin(start_elipse)
    figure, axes = plt.subplots(1)
    axes.plot(cos_x, sin_y, c='r', linestyle='--', )
    axes.set_aspect(1)


def draw_sin_plot(value: list[float]) -> None:
    x = np.linspace(start=value[0], stop=value[1], num=value[2])
    y = x ** 2 - 1
    plt.plot(x, y, c='y', label='sin')


def draw_dot_plot(x: list[float], y: list[float]) -> None:
    plt.scatter(x, y, c="blue", label='dot')


def draw_face(x_cos: list[float], y_curved: list[float], x: list[float], y: list[float], value: list[float]) -> None:
    draw_dashed_plot(x_cos, y_curved)
    draw_sin_plot(value)
    draw_dot_plot(x, y)
    plt.show()
