from abc import ABC, abstractmethod


class Graph(ABC):

    @abstractmethod
    def display_graphic(self, dist_image, dist_subject, focal_length, height_subject, height_image, is_real_image):
        """Метод, вызывающийся для построения графика"""

    @abstractmethod
    def default_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        """Построение осей координат"""

    @abstractmethod
    def build_subject(self, dist_subject, height_subject):
        """Построение предмета"""

    @abstractmethod
    def build_arrow(self, x1, x2, y1, y2, color="g", label="Изображение"):
        """Построение стрелок"""

    @abstractmethod
    def build_rays(self, dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image):
        """Построение лучей"""

    def calculate_coordinate(self, x1, x2, y1, y2, x=None, y=None):
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        if x is not None:
            return k * x + b
        if y is not None:
            return (y - b) / k
        return None