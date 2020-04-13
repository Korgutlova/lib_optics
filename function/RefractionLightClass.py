import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from util import errors


class RefractionLightClass:
    file_to_csv = "../files/list_of_refractive_indices.csv"

    def __init__(self):
        self.dictionary = self.init_dictionary()

    def init_dictionary(self):
        return pd.read_csv(self.file_to_csv, skiprows=1, header=None,
                           dtype={0: str, 1: np.float64}).set_index(0).squeeze().to_dict()

    """
    Get the angle of refraction based on the given parameters
    
    Parameters
    ----------
    
    angle_incidence : int 
        Angle in degrees 
    medium_one : float/int or str
        Эта среда откуда проходит луч, значение показателя преломления, или название среды
    medium_two : float/int or str
        Эта среда куда проходит луч, значение показателя преломления, или название среды
    """

    def get_angle_refraction(self, angle_incidence: float, medium_one, medium_two) -> float:
        medium_one, medium_two = self.__validate_index_name(medium_one, medium_two)
        """
        
        sin(a)/sin(y) = n2 / n1
        
        http://ru.solverbook.com/spravochnik/zakony-fiziki/zakon-prelomleniya-sveta/
        
        """
        # TODO try catch

        # синус (для вода/воздух 0,67, всё правильно)
        result_sin = math.sin(math.radians(angle_incidence)) * medium_one / medium_two
        if result_sin > 1:
            result_sin = -math.sin(math.radians(angle_incidence))
        # дальше надо взять арксинус и перевести в градусы
        return math.degrees(math.asin(result_sin))

    def __validate_index_name(self, medium_one, medium_two):
        if type(medium_one) == str:
            medium_one = self.get_refractive_index(medium_one)
        if type(medium_two) == str:
            medium_two = self.get_refractive_index(medium_two)
        return medium_one, medium_two

    def build_graph(self, angle_incidence: float, first_index, second_index):
        plt.annotate(first_index if type(first_index) == str else "Начальная среда", xy=(-1.5, 0.1))
        plt.annotate(second_index if type(second_index) == str else "Конечная среда", xy=(0.5, 0.1))
        first_index, second_index = self.__validate_index_name(first_index, second_index)
        second_angle = self.get_angle_refraction(angle_incidence, first_index, second_index)
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

    def get_refractive_index(self, media: str) -> float:
        index = self.dictionary.get(media.lower(), -1)
        if index != -1:
            return index
        else:
            raise errors.RefractiveIndexNotFound(media)

    def set_refractive_index(self, media: str, value: float):
        # TODO save data to csv file and to the "dictionary"
        pass

    def get_koef(self, x1, x2, y1, y2):
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        return k, b

    # пересечение между прямой и окружностью
    def get_discriminant(self, k, b, r):
        D = math.sqrt(abs(r * r * (k * k + 1) - b * b))
        x1 = ((-1) * k * b - D) / (1 + k * k)
        x2 = ((-1) * k * b + D) / (1 + k * k)
        return x1, x2

    def get_Y(self, x, k, b):
        return x * k + b

    def get_circle_coordinates(self, r):
        theta = np.linspace(0, 2 * np.pi, 1000)

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        return x, y

    def display_curves(self, x1, x2, y1, y2, x_1, x_2, y_1, y_2):
        r = 0.5

        self.__display_curve(x1, x2, y1, y2, r, True)
        self.__display_curve(x_1, x_2, y_1, y_2, r, False)

    def __display_curve(self, x1, x2, y1, y2, r, is_first):
        x, y = self.get_circle_coordinates(r)
        k, b = self.get_koef(x1, x2, y1, y2)
        x_1, x_2 = self.get_discriminant(k, b, r)
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
