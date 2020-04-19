from abc import abstractmethod
import matplotlib.pyplot as plt

from models.graphs.AbstractGraph import AbstractGraph


class LensGraph(AbstractGraph):

    def __init__(self):
        self._def_axes_color = "black"
        self._rays_color = "blue"
        self._focus_color = "red"

    def build_graph(self, dist_image, dist_subject, focal_length, height_subject, height_image, is_real_image):
        self.default_axis(dist_subject, dist_image, focal_length, height_subject, is_real_image)
        self.build_subject(dist_subject, height_subject)
        self.build_rays(dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image)
        plt.legend(loc='lower right', shadow=True, fontsize='x-large')
        plt.show()

    @property
    def def_axes_color(self):
        return self._def_axes_color

    @def_axes_color.setter
    def def_axes_color(self, value):
        self._def_axes_color = value

    @property
    def rays_color(self):
        return self._rays_color

    @rays_color.setter
    def rays_color(self, value):
        self._rays_color = value

    @property
    def focus_color(self):
        return self._focus_color

    @focus_color.setter
    def focus_color(self, value):
        self._focus_color = value

    @abstractmethod
    def default_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        """Построение осей координат"""

    @abstractmethod
    def build_subject(self, dist_subject, height_subject):
        """Построение предмета"""

    def build_arrow(self, x1, x2, y1, y2, color="g", label="Изображение"):
        plt.plot([x1, x2], [y1, y2], color, label=label)  # Object
        plt.plot([x1, x1 - 0.05 * y2], [y2, 0.85 * y2], color)  # Arrow Left
        plt.plot([x1, x1 + 0.05 * y2], [y2, 0.85 * y2], color)  # Arrow Right

    def build_focus(self, focal_length):
        plt.plot([focal_length, focal_length], [-0.5, 0.5], self._focus_color, label="Фокус")
        plt.plot([-focal_length, -focal_length], [-0.5, 0.5], self._focus_color)

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
