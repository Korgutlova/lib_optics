from abc import abstractmethod
import matplotlib.pyplot as plt

from models.graphs.AbstractGraph import AbstractGraph
from util import errors


class LensGraph(AbstractGraph):
    """Абстрактный класс для графиков с линзами"""
    _dash = "--"
    _point = "o"
    _colors = {"blue": "b", "green": "g", "red": "r", "cyan": "c",
               "magenta": "m", "yellow": "y", "black": "k", "white": "w"}

    def __init__(self):
        self._axes_color = "black"
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

        self._unit = "см"

    def build_graph(self, dist_subject, dist_image, height_subject, height_image, focal_length, is_real_image):
        """
        Метод, вызывающийся для построения графика с линзами

        Parameters
        ----------
        :param dist_subject: float
            Расстояние от линзы до объекта
        :param dist_image: float
            Расстояние от линзы до изображения
        :param height_subject: float
            Высота предмета
        :param height_image: float
            Высота изображения
        :param focal_length: float
            фокусное расстояние линзы
        :param is_real_image: bool
            Является изображение реальным или нет
        """
        self.build_axis(dist_subject, dist_image, focal_length, height_subject, is_real_image)
        self.build_subject(dist_subject, height_subject)
        self.build_rays(dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image)
        plt.legend(loc='lower right', shadow=True, fontsize='x-large')
        plt.xlabel("X, %s" % self._unit)
        plt.ylabel("Y, %s" % self._unit)
        plt.show()

    def build_subject(self, dist_subject, height_subject):
        """
        Построение объекта

        Parameters
        ----------
        :param dist_subject: float
            Расстояние от линзы до объекта
        :param height_subject: float
            Высота объекта
        """
        if height_subject != 0:
            self.build_arrow((-1) * dist_subject, (-1) * dist_subject, 0, height_subject, self._subject_color,
                             self._subject_label)
        else:
            plt.plot([(-1) * dist_subject, (-1) * dist_subject], [0, 0], self._subject_point, label=self._subject_label)

    def build_arrow(self, x1, x2, y1, y2, color, custom_label):
        """
        Построение стрелок

        Parameters
        ----------
        :param x1: float
            Координата x первой стрелки
        :param x2: float
            Координата x второй стрелки
        :param y1: float
            Координата y первой стрелки
        :param y2: float
            Координата y второй стрелки
        :param color: str
            Цвет стрелок
        :param custom_label: str
            Метка
        """
        plt.plot([x1, x2], [y1, y2], color, label=custom_label)
        plt.plot([x1, x1 - 0.05 * y2], [y2, 0.85 * y2], color)
        plt.plot([x1, x1 + 0.05 * y2], [y2, 0.85 * y2], color)

    def build_focus(self, focal_length):
        """
        Построение фокуса

        Parameters
        ----------
        :param focal_length: float
            Фокусное расстояние линзы
        """
        plt.plot([focal_length, focal_length], [-0.5, 0.5], self._focus_color, label="Фокус")
        plt.plot([-focal_length, -focal_length], [-0.5, 0.5], self._focus_color)

    @abstractmethod
    def build_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        """
        Построение осей координат

        Parameters
        ----------
        :param dist_subject: float
            Расстояние от линзы до объекта
        :param dist_image: float
            Расстояние от линзы до изображения
        :param height_subject: float
            Высота объекта
        :param focal_length: float
            фокусное расстояние линзы
        :param is_real_image: bool
            Является изображение реальным или нет
        """

    @abstractmethod
    def build_rays(self, dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image):
        """
        Построение лучей

        Parameters
        ----------
        :param dist_subject: float
            Расстояние от линзы до объекта
        :param dist_image: float
            Расстояние от линзы до изображения
        :param height_subject: float
            Высота объекта
        :param height_image: float
            Высота изображения
        :param focal_length: float
            фокусное расстояние линзы
        :param is_real_image: bool
            Является изображение реальным или нет
        """

    def calculate_coordinate(self, x1, x2, y1, y2, x=None, y=None):
        """
        Вычисление координаты точки на прямой по двум точкам и одной из координат

        Parameters
        ----------
        :param x1: float
            Координата x первой точки
        :param x2: float
            Координата x второй точки
        :param y1: float
            Координата y первой точки
        :param y2: float
            Координата y второй точки
        :param x: float
            Координата x искомой точки
        :param y: float
            Координата y искомой точки
        :returns вторая координата искомой точки, если задана хотя бы одна из координат, иначе None
        """
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        if x is not None:
            return k * x + b
        if y is not None:
            return (y - b) / k
        return None

    def _check_input_color(self, color):
        """
        Валидация цвета, поданного на вход

        Parameters
        ----------
        :param color: str
            Строковое значение цвета

        :raises ошибка InvalidArgumentStyleGraphic, если в качестве color передано не строковое значение
        """
        if color is None or not isinstance(color, str):
            raise errors.InvalidArgumentStyleGraphic("color должен быть строковым параметром")
        self._check_color_for_existence(color)

    def _check_input_label(self, label):
        """
        Валидация метки, поданной на вход

        Parameters
        ----------
        :param label: str
            Строковое значение метки

        :raises ошибка InvalidArgumentStyleGraphic, если в качестве label передано не строковое значение или если
            длина label превышает 20 символов
        """
        if label is None or not isinstance(label, str):
            raise errors.InvalidArgumentStyleGraphic("label должен быть строковым параметром")
        if len(label) > 20:
            raise errors.InvalidArgumentStyleGraphic("label не может превышать более 20 символов")

    def _check_color_for_existence(self, color):
        """
        Проверка существования цвета

        Parameters
        ----------
        :param color: str
            Строковое значение цвета

        :raises ошибка InvalidArgumentStyleGraphic, если цвета color не существует
        """
        for key, value in self._colors.items():
            if key == color or value == color:
                return
        raise errors.InvalidArgumentStyleGraphic(f"Цвета '{color}'не существует")

    def _get_marker_color(self, marker, value):
        """
        Получение цвета маркера

        Parameters
        ----------
        :param marker: str
            Форма маркера
        :param value: str
            Цвет маркера

        :returns код цвета маркера
        """
        return marker + (value if len(value) == 1 else self._colors[value])

    @property
    def axes_color(self):
        """
        axes_color: str
            Цвет осей координат
        """
        return self._axes_color

    @axes_color.setter
    def axes_color(self, value):
        """
        Добавление цвета осей координат

        Parameters
        ----------
        :param value: str
            Цвет осей координат
        """
        self._check_input_color(value)
        self._axes_color = value

    @property
    def rays_color(self):
        """
        rays_color: str
            Цвет лучей
        """
        return self._rays_color

    @rays_color.setter
    def rays_color(self, value):
        """
        Добавление цвета лучей

        Parameters
        ----------
        :param value: str
            Цвет лучей
        """
        self._check_input_color(value)
        self._rays_color = value
        self._rays_dash = self._get_marker_color(self._dash, value)

    @property
    def focus_color(self):
        """
        focus_color: str
            Цвет фокуса
        """
        return self._focus_color

    @focus_color.setter
    def focus_color(self, value):
        """
        Добавление цвета фокуса

        Parameters
        ----------
        :param value: str
            Цвет фокуса
        """
        self._check_input_color(value)
        self._focus_color = value
        self._focus_dash = self._get_marker_color(self._dash, value)

    @property
    def image_color(self):
        """
        image_color: str
            Цвет изображения
        """
        return self._image_color

    @image_color.setter
    def image_color(self, value):
        """
        Добавление цвета изображения

        Parameters
        ----------
        :param value: str
            Цвет изображения
        """
        self._check_input_color(value)
        self._image_color = value
        self._image_point = self._get_marker_color(self._point, value)
        self._image_dash = self._get_marker_color(self._dash, value)

    @property
    def subject_color(self):
        """
        subject_color: str
            Цвет предмета
        """
        return self._subject_color

    @subject_color.setter
    def subject_color(self, value):
        """
        Добавление цвета объекта

        Parameters
        ----------
        :param value: str
            Цвет объекта
        """
        self._check_input_color(value)
        self._subject_color = value
        self._subject_point = self._get_marker_color(self._point, value)

    @property
    def subject_label(self):
        """
        subject_label: str
            Метка объекта
        """
        return self._subject_label

    @subject_label.setter
    def subject_label(self, value):
        """
        Добавление метки объекта

        Parameters
        ----------
        :param value: str
            Метка объекта
        """
        self._check_input_label(value)
        self._subject_label = value

    @property
    def image_label(self):
        """
        image_label: str
            Метка изображения
        """
        return self._image_label

    @image_label.setter
    def image_label(self, value):
        """
        Добавление метки изображения

        Parameters
        ----------
        :param value: str
            Метка изображения
        """
        self._check_input_label(value)
        self._image_label = value

    @property
    def unit(self):
        """
        unit: str
            Единица измерения, отображаемая на графике
        """
        return self._unit

    @unit.setter
    def unit(self, value):
        """
        Добавление единицы измерения

        Parameters
        ----------
        :param value: str
            Единица измерения
        """
        self._unit = value
