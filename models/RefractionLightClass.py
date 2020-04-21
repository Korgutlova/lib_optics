import math
import numbers

import pandas as pd
import numpy as np

from models.graphs.RefractionGraph import RefractionGraph
from util import errors


class RefractionLightClass:
    """Класс для вычисления угла падения/отражения на границу раздела двух сред"""

    file_to_csv = "../files/list_of_refractive_indices.csv"
    graph = RefractionGraph()

    def __init__(self):
        self.dictionary = self.__init_base_dictionary()

    def __init_base_dictionary(self):
        """Загрузка библиотеки показателей преломления сред"""
        return pd.read_csv(self.file_to_csv, skiprows=1, header=None,
                           dtype={0: str, 1: np.float64}).set_index(0).squeeze().to_dict()

    def get_angle_refraction(self, angle_incidence: float, medium_one, medium_two) -> float:
        """
        Расчёт угла преломления

        Parameters
        ----------
        :param angle_incidence: float
            Угол падения
        :param medium_one: float
            Коэффициент преломления первой среды
        :param medium_two: float
            Коэффициент преломления второй среды
        :returns угол отражения
        """
        self.__check_angle(angle_incidence)
        _, medium_one = self.__validate_index_name(medium_one)
        _, medium_two = self.__validate_index_name(medium_two)
        result_sin = math.sin(math.radians(angle_incidence)) * medium_one / medium_two
        if result_sin > 1:
            result_sin = -math.sin(math.radians(angle_incidence))
        return math.degrees(math.asin(result_sin))

    def __validate_index_name(self, label):
        """
        Валидация имён сред

        Parameters
        ----------
        :param label: str
            Название среды

        :returns название среды, коэффициент преломления среды, если такая среда существует
        :raises ошибка InvalidRefractiveIndex, если в качестве label не строка или число или если такая среда не
            существует
        """
        type_m = type(label)
        if type_m == str:
            value = self.get_refractive_index(label)
        else:
            if isinstance(label, numbers.Number):
                value = label
                if value < 1 or value > 10:
                    raise errors.InvalidRefractiveIndex(f'Недопустимый индекс "{value}" для среды. '
                                                        f'Допустимый индекс должен входить в рамки [1, 10]')
            else:
                raise errors.InvalidRefractiveIndex(f'Недопустимый тип для индекса среды: "{type_m}"')
        return label, value

    def build_graph(self, angle_incidence: float, first_index, second_index):
        """
        Построение графика

        Parameters
        ----------
        :param angle_incidence: float
            Угол падения
        :param first_index: float
            Коэффициент преломления первой среды
        :param second_index: float
            Коэффициент преломления второй среды
        """
        first_label, first_index = self.__validate_index_name(first_index)
        second_label, second_index = self.__validate_index_name(second_index)
        second_angle = round(self.get_angle_refraction(angle_incidence, first_index, second_index))

        self.graph.build_graph(angle_incidence, first_label, first_index, second_label, second_index, second_angle)

    def get_refractive_index(self, media: str) -> float:
        """
        Получение показателя преломления среды

        Parameters
        ----------
        :param media: str
            Название среды

        :returns Коэффициент преломления среды media
        :raises ошибка RefractiveIndexNotFound, если среда media не существует
        """
        index = self.dictionary.get(media.lower(), -1)
        if index != -1:
            return index
        else:
            raise errors.RefractiveIndexNotFound(f'Индекс среды "{media}" не найден.')

    def set_refractive_indexes(self, file):
        """
        Добавление пользовательских показателей преломления среды

        Parameters
        ----------
        :param file: str
            Путь к пользовательскому файлу с коэффициентами преломления сред
        """
        self.dictionary.update(pd.read_csv(file, header=None,
                           dtype={0: str, 1: np.float64}).set_index(0).squeeze().to_dict())

    @staticmethod
    def __check_angle(angle):
        """
        Проверка валидности угла

        Parameters
        ----------
        :param angle: float
            Величина угла

        :raises ошибка InvalidArgumentForAngle, если в качестве angle передано не число или если angle выходит за
            пределы допустимых значений
        """
        if not isinstance(angle, numbers.Number):
            raise errors.InvalidArgumentForAngle(f'Недопустимый "{angle}" тип для угла')
        if angle <= 0 or angle >= 90:
            raise errors.InvalidArgumentForAngle(f'Угол "{angle}" некорректен. '
                                                 f'Допустимый угол должен входить в рамки (1; 90)')
