import numpy as np
import matplotlib.pyplot as plt
import copy

train1 = [
    1, 1, -1, -1, -1,
    -1, 1, -1, -1, -1,
    -1, 1, -1, -1, -1,
    -1, 1, -1, -1, -1,
    -1, 1, -1, -1, -1
]

train2 = [
    1, -1, -1, -1, 1,
    -1, 1, -1, 1, -1,
    -1, -1, 1, -1, -1,
    -1, 1, -1, 1, -1,
    1, -1, -1, -1, 1
]

train3 = [
    -1, -1, 1, -1, -1,
    -1, -1, 1, -1, -1,
    1, 1, 1, 1, 1,
    -1, -1, 1, -1, -1,
    -1, -1, 1, -1, -1
]

test1 = [
    -1, 1, -1, -1, -1,
    -1, 1, -1, -1, -1,
    -1, 1, -1, -1, -1,
    -1, 1, -1, -1, -1,
    -1, 1, -1, -1, -1
]

test2 = [
    1, 1, -1, -1, 1,
    -1, 1, -1, 1, -1,
    -1, 1, 1, 1, -1,
    -1, 1, -1, 1, -1,
    1, 1, -1, -1, 1
]

test3 = [
    -1, -1, -1, -1, -1,
    -1, -1, 1, -1, -1,
    1, 1, 1, 1, 1,
    -1, -1, -1, -1, -1,
    -1, -1, 1, -1, -1
]

test4 = [
    -1, 1, 1, 1, 1,
    1, -1, 1, 1, 1,
    1, -1, 1, 1, 1,
    1, -1, 1, 1, 1,
    1, -1, 1, 1, 1
]


class Hopfield:
    __img_train = []
    __img_test = []

    def __init__(self, height, width):
        self.n = height * width
        self.weights = np.zeros((self.n, self.n))

    def correction(self, img_train):
        for img_train_x in range(self.n):
            for img_train_y in range(self.n):
                if img_train_x != img_train_y:
                    self.weights[img_train_x][img_train_y] += round(
                        (1 / self.n) * img_train[img_train_x] * img_train[
                            img_train_y], 2)

        self.__img_train = img_train

    def recognise_img(self, img_test):
        self.__img_test = img_test
        self.plot()
        _copy = []
        while _copy != img_test:
            _copy = copy.deepcopy(img_test)
            for img_test_x in range(self.n):
                sum_neu_value = 0
                for img_test_y in range(self.n):
                    sum_neu_value += img_test[img_test_y] * self.weights[img_test_x][img_test_y]
                img_test[img_test_x] = 1 if sum_neu_value >= 0 else -1

        return img_test

    def plot(self):
        fig, (ax1, ax2) = plt.subplots(2)
        ax1.imshow(np.reshape(self.__img_train, (-1, 5)))
        ax1.set_title('train plot')
        ax2.imshow(np.reshape(self.__img_test, (-1, 5)))
        ax2.set_title('test plot')
        plt.tight_layout()
        plt.show()


hop = Hopfield(5, 5)

hop.correction(train3)
hop.recognise_img(test2)
