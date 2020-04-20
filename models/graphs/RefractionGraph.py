import math

from models.graphs.LensGraph import AbstractGraph
import matplotlib.pyplot as plt
import numpy as np


def get_circle_coordinates(r):
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


def get_koef(x1, x2, y1, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return k, b


# пересечение между прямой и окружностью
def get_discriminant(k, b, r):
    D = math.sqrt(abs(r * r * (k * k + 1) - b * b))
    x1 = ((-1) * k * b - D) / (1 + k * k)
    x2 = ((-1) * k * b + D) / (1 + k * k)
    return x1, x2


class RefractionGraph(AbstractGraph):
    def build_graph(self, angle_incidence: float, first_label, first_index, second_label, second_index, second_angle):
        plt.annotate(first_label if type(first_label) == str else "Начальная среда", xy=(-1.5, 0.1))
        plt.annotate(second_label if type(second_label) == str else "Конечная среда", xy=(0.5, 0.1))
        plt.annotate(angle_incidence, xy=(-0.6, -0.2))
        plt.annotate(math.floor(abs(second_angle)), xy=(0.5 if second_angle > 0 else -0.6, 0.3))
        first_x = 2 / math.tan(math.radians(angle_incidence))
        second_x = 2 / math.tan(math.radians(second_angle))
        self.display_curves(-first_x, 0, -2, 0, 0, second_x, 0, 2)
        plt.plot([-first_x, 0], [-2, 0])
        plt.plot([0, second_x], [0, 2])
        plt.axvline(x=0, color="black")
        plt.axhline(y=0, color="black")
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        frame = plt.gca()
        frame.axes.get_xaxis().set_ticks([])
        frame.axes.get_yaxis().set_ticks([])
        plt.show()

    def display_curves(self, x1, x2, y1, y2, x_1, x_2, y_1, y_2):
        r = 0.5

        self.__display_curve(x1, x2, y1, y2, r, True)
        self.__display_curve(x_1, x_2, y_1, y_2, r, False)

    def get_Y(self, x, k, b):
        return x * k + b

    def __display_curve(self, x1, x2, y1, y2, r, is_first):
        x, y = get_circle_coordinates(r)
        k, b = get_koef(x1, x2, y1, y2)
        x_1, x_2 = get_discriminant(k, b, r)
        if is_first:
            x_point = x_1 if x_1 < 0 else x_2
        else:
            if x2 > 0:
                x_point = x_1 if x_1 > 0 else x_2
            else:
                x_point = x_1 if x_1 < 0 else x_2
        y_point = self.get_Y(x_point, k, b)

        curve_x = []
        curve_y = []
        for elem1, elem2 in zip(x, y):
            if is_first:
                if np.sign(elem1) == np.sign(x_point) and np.sign(elem2) == np.sign(y_point) \
                        and elem2 >= y_point and elem1 <= x_point:
                    curve_x.append(elem1)
                    curve_y.append(elem2)
            else:
                if x2 > 0:
                    if np.sign(elem1) == np.sign(x_point) and np.sign(elem2) == np.sign(y_point) \
                            and elem2 <= y_point and elem1 >= x_point:
                        curve_x.append(elem1)
                        curve_y.append(elem2)
                else:
                    if np.sign(elem1) == np.sign(x_point) and np.sign(elem2) == np.sign(y_point) \
                            and elem2 <= y_point and elem1 <= x_point:
                        curve_x.append(elem1)
                        curve_y.append(elem2)

        plt.plot(curve_x, curve_y, "black")
