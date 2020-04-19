from abc import ABC, abstractmethod


class AbstractGraph(ABC):

    @abstractmethod
    def build_graph(self, angle_incidence: float, first_index, second_index, second_angle):
        """Метод, вызывающийся для построения графика"""
