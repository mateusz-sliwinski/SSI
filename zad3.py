from math import sqrt

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import zad1


def distance(x: list[float], y: list[float]) -> float:
    return sqrt(sum(abs(i1 - i2) for i1, i2 in zip(x, y)))


def argmin(iterable):
    return min(enumerate(iterable), key=lambda _: _[1])[0]


class KMean:
    def __init__(self, data: zad1.DecisionSystem, groups: int, iteration: int) -> None:
        self.data = data
        self.groups = groups
        self.iteration = iteration

    def km(self):
        data = self.data
        take_out = data.get_all_object_float([_ for _ in range(0, 101)], [_ for _ in range(0, 2)])
        take_group_without_repetition = take_out.sample(replace=False, n=self.groups)

        list_rand_x, list_rand_y = [], []
        list_value_col_x, list_value_col_y = [], []
        metric_value_list = []
        temp_list, final_list = [], []
        index_list = []

        for rand_x, rand_y in take_group_without_repetition.itertuples(index=False):
            list_rand_x.append(rand_x)
            list_rand_y.append(rand_y)

        for value_col_x, value_col_y in take_out.itertuples(index=False):
            list_value_col_x.append(value_col_x)
            list_value_col_y.append(value_col_y)

        for main in range(self.iteration):
            for x in range(len(list_value_col_x)):
                for length in range(self.groups):
                    metric_value_list.append(
                        distance(
                            [list_value_col_x[x], list_value_col_y[x]],
                            [list_rand_x[length], list_rand_y[length]]
                        )
                    )

                    if len(metric_value_list) == self.groups:
                        final_list.append(metric_value_list.copy())
                        metric_value_list.clear()

            for index in final_list:
                index_list.append(argmin(index))

            sum_x = 0
            sum_y = 0

            list_rand_x.clear()
            list_rand_y.clear()

            for y in range(self.groups):
                for x in range(len(index_list)):
                    if index_list[x] == y:
                        sum_x += list_value_col_x[x]
                        sum_y += list_value_col_y[x]
                list_rand_x.append(sum_x / index_list.count(y))
                list_rand_y.append(sum_y / index_list.count(y))
                sum_x = 0
                sum_y = 0

            print(str(list_rand_x) + ' ' + str(list_rand_y))

            colors = ['red', 'black', 'grey', 'orange', 'magenta']
            for x in range(len(take_out)):
                for y in range(101):
                    if index_list[x] == y:
                        plt.plot(take_out[0][x], take_out[1][x], marker="o", color=colors[y])

            for x in range(len(list_rand_x)):
                plt.plot(list_rand_x[x], list_rand_y[x], marker="v", color='green')

            red_patch = mpatches.Patch(color='red', label='group 1')
            black_patch = mpatches.Patch(color='black', label='group 2')
            grey_patch = mpatches.Patch(color='grey', label='group 3')
            orange_patch = mpatches.Patch(color='orange', label='group 4')
            magenta_patch = mpatches.Patch(color='magenta', label='group 5')
            marker_patch = mpatches.Patch(color='green', label='marker v')

            plt.legend(
                loc=2, prop={'size': 6},
                handles=[red_patch, black_patch, grey_patch, orange_patch, magenta_patch, marker_patch])
            plt.show()

            index_list.clear()
            final_list.clear()


x = KMean(zad1.DecisionSystem('data/spirala.txt', 'data/spirala-type.txt'), 5, 5)

x.km()
