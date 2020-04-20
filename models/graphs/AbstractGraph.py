from abc import ABC, abstractmethod


class AbstractGraph(ABC):
    """Абстрактный класс для построения и отображения графиков"""

    @abstractmethod
    def build_graph(self, *args):
        """
        Абстрактный метод, который должен быть переопределён наследниками класса. Вызывается для построения графика
        """
