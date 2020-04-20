import math

import numpy as np


class MathHelper:
    """Класс для вычисления различных математических формул"""

    @staticmethod
    def get_circle_coordinates(r):
        """
        Метод расчёта координат дуг углов

        Parameters
        ----------
        :param r: float
            Радиус дуги

        :returns списки координат двух дуг
        """
        theta = np.linspace(0, 2 * np.pi, 1000)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return x, y

    @staticmethod
    def get_koef(x1, x2, y1, y2):
        """
        Метод расчёта коэффициента в уравнении прямой
        Parameters
        ----------
        :param x1: float
            Координата x первой точки
        :param x2: float
            Координата x второй точки
        :param y1: float
            Координата y первой точки
        :param y2: float
            Координата y второй точки

        :returns коэффициенты k, b
        """
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        return k, b

    @staticmethod
    def find_roots(k, b, r):
        """
        Метод для расчёта корней уравнения

        Parameters
        ----------
        :param k: float
            Коэффициент k
        :param b: float
            Коэффициент b
        :param r: float
            Коэффициент r - радиус дуги

        :returns x1, x2 - корни уравнения
        """
        D = math.sqrt(abs(r * r * (k * k + 1) - b * b))
        x1 = ((-1) * k * b - D) / (1 + k * k)
        x2 = ((-1) * k * b + D) / (1 + k * k)
        return x1, x2