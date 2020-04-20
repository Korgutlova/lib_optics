from abc import abstractmethod
import matplotlib.pyplot as plt

from models.graphs.AbstractGraph import AbstractGraph


class LensGraph(AbstractGraph):
    """Абстрактный класс для графиков с линзами"""
    _dash = "--"
    _point = "o"

    def __init__(self):
        self._axes_color = "black"
        self._rays_color = "blue"
        self._rays_dash = self._dash + "b"
        self._focus_color = "red"
        self._focus_dash = self._dash + "r"
        self._image_color = "green"
        self._subject_color = "green"
        self._subject_point = self._point + "g"
        self._image_point = self._point + "g"
        self._subject_dash = self._dash + "g"
        self._subject_label = "Объект"
        self._image_label = "Изображение"

    def build_graph(self, dist_image, dist_subject, focal_length, height_subject, height_image, is_real_image):
        """Метод, вызывающийся для построения графика с линзами"""
        self.build_axis(dist_subject, dist_image, focal_length, height_subject, is_real_image)
        self.build_subject(dist_subject, height_subject)
        self.build_rays(dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image)
        plt.legend(loc='lower right', shadow=True, fontsize='x-large')
        plt.show()

    def build_subject(self, dist_subject, height_subject):
        """Построение предмета"""
        if height_subject != 0:
            self.build_arrow((-1) * dist_subject, (-1) * dist_subject, 0, height_subject, self._subject_color,
                             self._subject_label)
        else:
            plt.plot([(-1) * dist_subject, (-1) * dist_subject], [0, 0], self._subject_point, self._subject_label)

    def build_arrow(self, x1, x2, y1, y2, color, custom_label):
        """Построение стрелок"""
        plt.plot([x1, x2], [y1, y2], color, label=custom_label)
        plt.plot([x1, x1 - 0.05 * y2], [y2, 0.85 * y2], color)
        plt.plot([x1, x1 + 0.05 * y2], [y2, 0.85 * y2], color)

    def build_focus(self, focal_length):
        """Построение фокуса"""
        plt.plot([focal_length, focal_length], [-0.5, 0.5], self._focus_color, label="Фокус")
        plt.plot([-focal_length, -focal_length], [-0.5, 0.5], self._focus_color)

    @abstractmethod
    def build_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        """Построение осей координат"""

    @abstractmethod
    def build_rays(self, dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image):
        """Построение лучей"""

    def calculate_coordinate(self, x1, x2, y1, y2, x=None, y=None):
        """Вычисление координаты точки на прямой по заданной точке и одной из координат"""
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        if x is not None:
            return k * x + b
        if y is not None:
            return (y - b) / k
        return None

    @property
    def axes_color(self):
        """Цвет осей координат"""
        return self._axes_color

    @axes_color.setter
    def axes_color(self, value):
        """Сеттер цвета осей координат"""
        self._axes_color = value

    @property
    def rays_color(self):
        """Цвет лучей"""
        return self._rays_color

    @rays_color.setter
    def rays_color(self, value):
        """Сеттер цвета лучей"""
        self._rays_color = value

    @property
    def focus_color(self):
        """Цвет фокуса"""
        return self._focus_color

    @focus_color.setter
    def focus_color(self, value):
        """Сеттер цвета фокуса"""
        self._focus_color = value

    @property
    def image_color(self):
        """Цвет изображения"""
        return self._image_color

    @image_color.setter
    def image_color(self, value):
        """Сеттер цвета изображения"""
        self._image_color = value

    @property
    def subject_color(self):
        """Цвет предмета"""
        return self._subject_color

    @subject_color.setter
    def subject_color(self, value):
        """Сеттер цвета предмета"""
        self._subject_color = value

    @property
    def subject_label(self):
        """Метка предмета"""
        return self._subject_label

    @subject_label.setter
    def subject_label(self, value):
        """Сеттер метки предмета"""
        self._subject_label = value

    @property
    def image_label(self):
        """Метка изображения"""
        return self._image_label

    @image_label.setter
    def image_label(self, value):
        """Сеттер метки изображения"""
        self._image_label = value
