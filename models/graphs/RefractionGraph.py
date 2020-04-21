import math

from models.graphs.LensGraph import AbstractGraph
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

from util import errors
from util.MathHelper import MathHelper


class RefractionGraph(AbstractGraph):
    """Класс графика для отражения/преломления"""

    def __init__(self):
        self._axes_color = "black"
        self._first_angle_color = "red"
        self._second_angle_color = "blue"
        self._first_ray_color = "blue"
        self._second_ray_color = "orange"
        self._first_medium_color = "aquamarine"
        self._second_medium_color = "teal"
        self._first_medium = "Начальная среда"
        self._second_medium = "Конечная среда"
        self._y_min = -2
        self._y_max = 2
        self._x_min = -2
        self._x_max = 2
        self._radius = 0.5

    def _get_color(self, value):
        """
        Получение кода цвета из библиотеки цветов CSS Colors

        Parameters
        ----------
        :param value: str
            Название цвета

        :returns код цвета
        :raises ошибка InvalidArgumentStyleGraphic, если такого цвета не существует
        """
        try:
            return mcolors.CSS4_COLORS[value]
        except KeyError:
            raise errors.InvalidArgumentStyleGraphic(f"Цвета '{value}' не существует")

    @property
    def axes_color(self):
        """
        axes_color: str
            Цвет осей координат
        """
        return self._axes_color

    @axes_color.setter
    def axes_color(self, value):
        """
        Добавление цвета осей координат

        Parameters
        ----------
        :param value: str
            Цвет осей координат
        """
        self._axes_color = self._get_color(value)

    @property
    def first_angle_color(self):
        """
        first_angle_color: str
            Цвет первого угла
        """
        return self._first_angle_color

    @first_angle_color.setter
    def first_angle_color(self, value):
        """
        Добавление цвета первого угла

        Parameters
        ----------
        :param value: str
            Цвет первого угла
        """
        self._first_angle_color = self._get_color(value)

    @property
    def second_angle_color(self):
        """
        second_angle_color: str
            Цвет второго угла
        """
        return self._second_angle_color

    @second_angle_color.setter
    def second_angle_color(self, value):
        """
        Добавление цвета второго угла

        Parameters
        ----------
        :param value: str
            Цвет второго угла
        """
        self._second_angle_color = self._get_color(value)

    @property
    def first_ray_color(self):
        """
        first_ray_color: str
            Цвет первого луча
        """
        return self._first_ray_color

    @first_ray_color.setter
    def first_ray_color(self, value):
        """
        Добавление цвета первого луча

        Parameters
        ----------
        :param value: str
            Цвет первого луча
        """
        self._first_ray_color = self._get_color(value)

    @property
    def second_ray_color(self):
        """
        second_ray_color: str
            Цвет второго луча
        """
        return self._second_ray_color

    @second_ray_color.setter
    def second_ray_color(self, value):
        """
        Добавление цвета второго луча

        Parameters
        ----------
        :param value: str
            Цвет второго луча
        """
        self._second_ray_color = self._get_color(value)

    @property
    def first_medium_color(self):
        """
        first_medium_color: str
            Цвет первой среды
        """
        return self._first_medium_color

    @first_medium_color.setter
    def first_medium_color(self, value):
        """
        Добавление цвета первой среды

        Parameters
        ----------
        :param value: str
            Цвет первой среды
        """
        self._first_medium_color = self._get_color(value)

    @property
    def second_medium_color(self):
        """
        second_medium_color: str
            Цвет второй среды
        """
        return self._second_medium_color

    @second_medium_color.setter
    def second_medium_color(self, value):
        """
        Добавление цвета второй среды

        Parameters
        ----------
        :param value: str
            Цвет второй среды
        """
        self._second_medium_color = self._get_color(value)

    @property
    def first_medium(self):
        """
        first_medium: str
            label первой среды
        """
        return self._first_medium

    @first_medium.setter
    def first_medium(self, value):
        """
        Добавление label первой среды

        Parameters
        ----------
        :param value: str
            label первой среды
        """
        self._first_medium = value

    @property
    def second_medium(self):
        """
        second_medium: str
            label второй среды
        """
        return self._second_medium

    @second_medium.setter
    def second_medium(self, value):
        """
        Добавление label второй среды

        Parameters
        ----------
        :param value: str
            label второй среды
        """
        self._second_medium = value

    def build_graph(self, angle_incidence: float, first_label, first_index, second_label, second_index, second_angle):
        """
        Построение графика преломления

        Parameters
        ----------
        :param angle_incidence: float
            Первый угол
        :param first_label: str
            Название первой среды
        :param first_index: float
            Коэффициент преломления первой среды
        :param second_label: str
            Название второй среды
        :param second_index: float
            Коэффициент преломления второй среды
        :param second_angle: float
            Второй угол
        """
        plt.annotate(first_label if type(first_label) == str else self._first_medium, xy=(-1.5, 0.1))
        plt.annotate(second_label if type(second_label) == str else self._second_medium, xy=(0.5, 0.1))
        plt.annotate(angle_incidence, xy=(-0.6, -0.2))
        plt.annotate(math.floor(abs(second_angle)), xy=(0.5 if second_angle > 0 else -0.6, 0.3))
        first_x = 2 / math.tan(math.radians(angle_incidence))
        second_x = 2 / math.tan(math.radians(second_angle))
        self.__display_curve(-first_x, 0, self._y_min, 0, True)
        self.__display_curve(0, second_x, 0, self._y_max, False)
        plt.plot([-first_x, 0], [self._y_min, 0], color=self._first_ray_color)
        plt.plot([0, second_x], [0, self._y_max], color=self._second_ray_color)
        plt.axvline(x=0, color=self._axes_color)
        plt.axhline(y=0, color=self._axes_color)
        plt.xlim([self._x_min, self._x_max])
        plt.ylim([self._y_min, self._y_max])
        self.fill_area(self._x_min, 0, self._y_min, self._y_max, self._first_medium_color)
        self.fill_area(0, self._x_max, self._y_min, self._y_max, self._second_medium_color)
        frame = plt.gca()
        frame.axes.get_xaxis().set_ticks([])
        frame.axes.get_yaxis().set_ticks([])
        plt.show()

    def fill_area(self, x_min, x_max, y_min, y_max, color):
        """
        Заливка цветом определенной области

        Parameters
        ----------
        :param x_min: float
            Нижняя граница по X
        :param x_max: float
            Верхняя граница по X
        :param y_min: float
            Нижняя граница по Y
        :param y_max: float
            Верхняя граница по Y
        :param color: str
            Цвет
        """
        x = np.arange(x_min, x_max, 0.01)
        y1 = [float(y_min) for i in range(len(x))]
        y2 = [float(y_max) for i in range(len(x))]

        plt.fill_between(x, y1, y2, color=color)

    def get_Y(self, x, k, b):
        """
        Вычисление координаты y по уравнению прямой

        Parameters
        ----------
        :param x: float
            Значение x на прямой
        :param k: float
            Коэффициент k
        :param b: float
            Коэффициент b

        :returns y
        """
        return x * k + b

    def __display_curve(self, x1, x2, y1, y2, is_first):
        """
        Отображение дуги угла

        Parameters
        ----------
        :param x1: float
            Координата x первой точки прямой
        :param x2: float
            Координата x второй точки прямой
        :param y1: float
            Координата y первой точки прямой
        :param y2: float
            Координата y второй точки прямой
        :param is_first: bool
            Образован ли этот угол падающим лучом
        """
        x, y = MathHelper.get_circle_coordinates(self._radius)
        k, b = MathHelper.get_koef(x1, x2, y1, y2)
        x_1, x_2 = MathHelper.find_roots(k, b, self._radius)
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

        plt.plot(curve_x, curve_y, self._first_angle_color if is_first else self._second_angle_color)
