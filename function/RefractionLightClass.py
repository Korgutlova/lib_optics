import math

import pandas as pd
import numpy as np


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

    # translate please
    def get_angle_refraction(self, angle_incidence, medium_one, medium_two):
        if type(medium_one) == str and type(medium_one) == str:
            medium_one = self.get_refractive_index(medium_one)
            medium_two = self.get_refractive_index(medium_two)
        """
        
        sin(a)/sin(y) = n2 / n1
        
        http://ru.solverbook.com/spravochnik/zakony-fiziki/zakon-prelomleniya-sveta/
        
        [how get degrees in end?]
        
        I tried math.degrees(result) -> but this didn't match in the answers of the tasks
        
        """
        # TODO try catch

        # синус (для вода/воздух 0,67, всё правильно)
        result_sin = math.sin(math.radians(angle_incidence)) * medium_one / medium_two
        # дальше надо взять арксинус и перевести в градусы
        return math.degrees(math.asin(result_sin))

    def get_refractive_index(self, media):
        # TODO check keyerror
        return self.dictionary[media.lower()]
