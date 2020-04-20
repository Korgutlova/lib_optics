from abc import ABC, abstractmethod


class AbstractGraph(ABC):
    """Абстрактный класс для построения и отображения графиков"""

    @abstractmethod
    def build_graph(self, *args):
        """Метод, вызывающийся для построения графика"""
