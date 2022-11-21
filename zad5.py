import numpy as np

BA = np.matrix(
    [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
    ]
)
BB = np.matrix(
    [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
    ]
)


def greedy_point(BA, BB):
    measure = 0
