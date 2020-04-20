from abc import abstractmethod
import matplotlib.pyplot as plt

from models.graphs.AbstractGraph import AbstractGraph
from util import errors


class LensGraph(AbstractGraph):
    _dash = "--"
    _point = "o"
    _colors = {"blue": "b", "green": "g", "red": "r", "cyan": "c",
               "magenta": "m", "yellow": "y", "black": "k", "white": "w"}

    def __init__(self):
        self._def_axes_color = "black"
        self._rays_color = "blue"
        self._rays_dash = self._dash + "b"

        self._focus_color = "red"
        self._focus_dash = self._dash + "r"

        self._subject_color = "green"
        self._subject_point = self._point + "g"
        self._subject_label = "Объект"

        self._image_color = "green"
        self._image_point = self._point + "g"
        self._image_dash = self._dash + "g"
        self._image_label = "Изображение"

    def build_graph(self, dist_image, dist_subject, focal_length, height_subject, height_image, is_real_image):
        self.default_axis(dist_subject, dist_image, focal_length, height_subject, is_real_image)
        self.build_subject(dist_subject, height_subject)
        self.build_rays(dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image)
        plt.legend(loc='lower right', shadow=True, fontsize='x-large')
        plt.show()

    @abstractmethod
    def default_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        """Построение осей координат"""

    def build_subject(self, dist_subject, height_subject):
        if height_subject != 0:
            self.build_arrow((-1) * dist_subject, (-1) * dist_subject, 0, height_subject, self._subject_color,
                             self._subject_label)
        else:
            plt.plot([(-1) * dist_subject, (-1) * dist_subject], [0, 0], self._subject_point, label=self._subject_label)

    def build_arrow(self, x1, x2, y1, y2, color, custom_label):
        plt.plot([x1, x2], [y1, y2], color, label=custom_label)
        plt.plot([x1, x1 - 0.05 * y2], [y2, 0.85 * y2], color)
        plt.plot([x1, x1 + 0.05 * y2], [y2, 0.85 * y2], color)

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

    def _check_input_color(self, color):
        if color is None:
            raise errors.InvalidArgumentStyleGraphic("color не может быть равен None")
        if not isinstance(color, str):
            raise errors.InvalidArgumentStyleGraphic("color должен быть строковым параметром")
        self._check_color_for_existence(color)

    def _check_input_label(self, label):
        if label is None:
            raise errors.InvalidArgumentStyleGraphic("label не может быть равен None")
        if not isinstance(label, str):
            raise errors.InvalidArgumentStyleGraphic("label должен быть строковым параметром")
        if len(label) > 20:
            raise errors.InvalidArgumentStyleGraphic("label не может превышать более 20 символов")

    def _check_color_for_existence(self, color):
        for key, value in self._colors.items():
            if key == color or value == color:
                return
        raise errors.InvalidArgumentStyleGraphic(f"Цвета '{color}'не существует")

    def _get_marker_color(self, marker, value):
        return marker + (value if len(value) == 1 else self._colors[value])

    @property
    def def_axes_color(self):
        return self._def_axes_color

    @def_axes_color.setter
    def def_axes_color(self, value):
        self._check_input_color(value)
        self._def_axes_color = value

    @property
    def rays_color(self):
        return self._rays_color

    @rays_color.setter
    def rays_color(self, value):
        self._check_input_color(value)
        self._rays_color = value
        self._rays_dash = self._get_marker_color(self._dash, value)

    @property
    def focus_color(self):
        return self._focus_color

    @focus_color.setter
    def focus_color(self, value):
        self._check_input_color(value)
        self._focus_color = value
        self._focus_dash = self._get_marker_color(self._dash, value)

    @property
    def image_color(self):
        return self._image_color

    @image_color.setter
    def image_color(self, value):
        self._check_input_color(value)
        self._image_color = value
        self._image_point = self._get_marker_color(self._point, value)
        self._image_dash = self._get_marker_color(self._dash, value)
        print(self._image_dash, self._image_point, self.image_color)

    @property
    def subject_color(self):
        return self._subject_color

    @subject_color.setter
    def subject_color(self, value):
        self._check_input_color(value)
        self._subject_color = value
        self._subject_point = self._get_marker_color(self._point, value)

    @property
    def subject_label(self):
        return self._subject_label

    @subject_label.setter
    def subject_label(self, value):
        self._check_input_label(value)
        self._subject_label = value

    @property
    def image_label(self):
        return self._image_label

    @image_label.setter
    def image_label(self, value):
        self._check_input_label(value)
        self._image_label = value
