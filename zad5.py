import math
from math import sqrt

import numpy as np
from matplotlib import pyplot as plt

test1 = [[0, 0, 0, 0],
         [0, 0, 1, 1],
         [0, 1, 1, 1],
         [0, 0, 0, 1],
         [0, 0, 0, 1]]

test2 = [[1, 1, 1, 1],
         [0, 0, 0, 1],
         [1, 1, 1, 1],
         [0, 0, 1, 1],
         [1, 1, 1, 1]]

test3 = [[1, 1, 1, 1],
         [0, 0, 0, 1],
         [0, 0, 1, 0],
         [1, 1, 0, 0],
         [1, 1, 1, 1]]

formula1 = [[0, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1]]

formula2 = [[0, 1, 1, 1],
            [1, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

formula3 = [[1, 1, 1, 0],
            [0, 0, 0, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 0]]

formula_list = [formula1, formula2, formula3]
test_list = [test1, test2, test3]


def distance_euclidesa(x: list[float], y: list[float]) -> float:
    return sqrt(sum(abs(i1 - i2) for i1, i2 in zip(x, y)))


def greedy_point(BA, BB):
    measure = 0

    for bitmap_test_x in range(len(BA)):
        for bitmap_test_y in range(len(BA[bitmap_test_x])):
            distance_min = math.inf
            if BA[bitmap_test_x][bitmap_test_y] == 1:

                for bitmap_formula_x in range(len(BB)):
                    for bitmap_formula_y in range(len(BB[bitmap_formula_x])):
                        if BB[bitmap_formula_x][bitmap_formula_y] == 1 and distance_min > distance_euclidesa(
                                [bitmap_test_x, bitmap_test_y], [bitmap_formula_x, bitmap_formula_y]):
                            distance_min = distance_euclidesa(
                                [bitmap_test_x, bitmap_test_y],
                                [bitmap_formula_x, bitmap_formula_y]
                            )
                measure += distance_min

    return measure


def measure_similarity_objective(BA, BB):
    return -(greedy_point(BA, BB) + greedy_point(BB, BA))


count = 0
for all_test_list in test_list:
    empty_list = []
    count += 1
    for all_formula_list in formula_list:
        empty_list.append(measure_similarity_objective(all_test_list, all_formula_list))

    x = empty_list.index(max(empty_list))
    fig, (ax1, ax2) = plt.subplots(2)

    ax1.imshow(formula_list[x])
    ax1.set_title('formula plot')
    ax2.imshow(all_test_list)
    ax2.set_title('test plot')
    plt.tight_layout()
    plt.show()

    print(f'{count} for that {x + 1}')
