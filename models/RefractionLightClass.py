import math
import numbers

import pandas as pd
import numpy as np

from models.graphs.RefractionGraph import RefractionGraph
from util import errors


class RefractionLightClass:
    file_to_csv = "../files/list_of_refractive_indices.csv"
    graph = RefractionGraph()

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
        self.__check_angle(angle_incidence)
        medium_one = self.__validate_index_name(medium_one)
        medium_two = self.__validate_index_name(medium_two)
        result_sin = math.sin(math.radians(angle_incidence)) * medium_one / medium_two
        if result_sin > 1:
            result_sin = -math.sin(math.radians(angle_incidence))
        return math.degrees(math.asin(result_sin))

    def __validate_index_name(self, medium):
        type_m = type(medium)
        if type_m == str:
            medium = self.get_refractive_index(medium)
        else:
            if isinstance(medium, numbers.Number):
                if medium < 1 or medium > 10:
                    raise errors.InvalidRefractiveIndex(f'Недопустимый индекс "{medium}" для среды. '
                                                        f'Допустимый индекс должен входить в рамки [1, 10]')
            else:
                raise errors.InvalidRefractiveIndex(f'Недопустимый "{type_m}" тип для индекса среды')
        return medium

    def build_graph(self, angle_incidence: float, first_index, second_index):
        first_index = self.__validate_index_name(first_index)
        second_index = self.__validate_index_name(second_index)
        second_angle = self.get_angle_refraction(angle_incidence, first_index, second_index)

        self.graph.build_graph(angle_incidence, first_index, second_index, second_angle)

    def get_refractive_index(self, media: str) -> float:
        index = self.dictionary.get(media.lower(), -1)
        if index != -1:
            return index
        else:
            raise errors.RefractiveIndexNotFound(media)

    def set_refractive_index(self, media: str, value: float):
        # TODO save data to csv file and to the "dictionary"
        pass

    @staticmethod
    def __check_angle(angle):
        if not isinstance(angle, numbers.Number):
            raise errors.InvalidArgumentForAngle(f'Недопустимый "{angle}" тип для угла')
        if angle <= 0 or angle >= 90:
            raise errors.InvalidArgumentForAngle(f'Угол "{angle}" некорректен. '
                                                 f'Допустимый угол должен входить в рамки (1; 90)')
