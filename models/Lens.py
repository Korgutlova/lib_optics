from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numbers

from util import errors


class Lens(ABC):
    _max_limit_value = 100

    _min_limit_vale = 0

    _pattern_invalid_argument = "Неверный тип аргумента '%s' для параметра %s. Тип данных должен быть %s."

    _pattern_over_limit_argument = "Аргумент '%s' для параметра %s выходит за пределы установленного лимита. " \
                                   f"Допустимые значения от {_min_limit_vale} до {_max_limit_value}."

    def __init__(self, dist_subject=None, dist_image=None, focal_length=None, real_image=None,
                 real_subject=None, height_subject=None, height_image=None):

        self._check_input_bool(real_subject, "real_subject")
        self._check_input_bool(real_subject, "real_image")

        self._check_input_numbers(height_image, "dist_subject")
        self._check_input_numbers(height_image, "dist_image")
        self._check_input_numbers(height_image, "focal_length")
        self._check_input_numbers(height_image, "height_subject")
        self._check_input_numbers(height_image, "height_image")

        self._real_subject = real_subject
        self._real_image = real_image
        self._dist_subject = dist_subject
        self._dist_image = dist_image
        self._focal_length = focal_length
        self._height_subject = height_subject
        self._height_image = height_image

    def __str__(self):
        return "F - %s\nf - %s\nd - %s" % (self._focal_length, self._dist_image, self._dist_subject)

    @property
    def real_subject(self):
        return self._real_subject

    @real_subject.setter
    def real_subject(self, value):
        self._check_input_bool(value, "real_subject")
        self._real_subject = value

    @property
    def real_image(self):
        return self._real_image

    @real_image.setter
    def real_image(self, value):
        self._check_input_bool(value, "real_image")
        self._real_image = value

    @property
    def dist_subject(self):
        return self._dist_subject

    @dist_subject.setter
    def dist_subject(self, value):
        self._check_input_numbers(value, "dist_subject")
        self._dist_subject = value

    @property
    def dist_image(self):
        return self._dist_image

    @dist_image.setter
    def dist_image(self, value):
        self._check_input_numbers(value, "dist_image")
        self._dist_image = value

    @property
    def focal_length(self):
        return self._focal_length

    @focal_length.setter
    def focal_length(self, value):
        self._check_input_numbers(value, "focal_length")
        self._focal_length = value

    @property
    def height_subject(self):
        return self._height_subject

    @height_subject.setter
    def height_subject(self, value):
        self._check_input_numbers(value, "height_subject")
        self._height_subject = value

    @property
    def height_image(self):
        return self._height_image

    @height_image.setter
    def height_image(self, value):
        self._check_input_numbers(value, "height_image")
        self._height_image = value

    def _check_input_numbers(self, value, name):
        if value is not None and not isinstance(value, numbers.Number):
            raise errors.InvalidArgumentForLens(self._pattern_invalid_argument % (value, name, "Number"))

        if not self._compare_with_limit(value):
            raise errors.InvalidArgumentForLens(self._pattern_over_limit_argument % (value, name))

    def _check_input_bool(self, value, name):
        if value is not None and not isinstance(value, bool):
            raise errors.InvalidArgumentForLens(self._pattern_invalid_argument % (value, name, "bool"))

    def _compare_with_limit(self, param):
        if param is None:
            return True
        return self._max_limit_value >= param >= self._min_limit_vale

    def check_not_none_for_F(self):
        return self._dist_subject is not None and self._dist_image is not None

    def check_not_none_for_d(self):
        return self._focal_length is not None and self._dist_image is not None

    def check_not_none_for_f(self):
        return self._focal_length is not None and self._dist_subject is not None

    # оптическая сила линзы - D
    def get_optical_power(self):
        return 1 / self._focal_length if self._focal_length is not None else None

    # увеличение линзы - Г
    def get_lens_enlargement(self):
        return self._dist_image / self._dist_subject \
            if self._dist_image is not None and self._dist_subject is not None else None

    # фокусное расстояние линзы - F
    @abstractmethod
    def get__focal_length(self):
        """Фокальное расстояние линзы"""

    # расстояние от линзы до предмета - d
    @abstractmethod
    def get__dist_subject(self):
        """Расстояние от линзы до объекта"""

    # расстояние от линзы до изображения - f
    @abstractmethod
    def get__dist_image(self):
        """Расстояние от линзы до предмета"""

    @abstractmethod
    def display_graphic(self):
        """Отображение графика"""

    @abstractmethod
    def default_axis(self):
        """Отображение осей"""

    @abstractmethod
    def build_rays(self):
        """Отображение лучей"""

    @abstractmethod
    def build_graph(self):
        """Метод, который нужно вызвать для постройки и отображения графика"""

    def build_arrow(self, x1, x2, y1, y2, color="g", label="Изображение"):
        plt.plot([x1, x2], [y1, y2], color, label=label)  # Object
        plt.plot([x1, x1 - 0.05 * y2], [y2, 0.85 * y2], color)  # Arrow Left
        plt.plot([x1, x1 + 0.05 * y2], [y2, 0.85 * y2], color)  # Arrow Right

    def build_object(self):
        if self._height_subject != 0:
            self.build_arrow((-1) * self._dist_subject, (-1) * self._dist_subject, 0, self._height_subject,
                             label="Объект")
        else:
            plt.plot([(-1) * self._dist_subject, (-1) * self._dist_subject], [0, 0], "go", label="Объект")  # Object

    def calculate_coordinate(self, x1, x2, y1, y2, x=None, y=None):
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        if x is not None:
            return k * x + b
        if y is not None:
            return (y - b) / k
        return None


class LensInterface(ABC):

    @abstractmethod
    def __str__(self):
        """Строковое отображение"""

    @abstractmethod
    def _check_input_numbers(self, value, name):
        """Проверка входных числовых аргументов"""

    @abstractmethod
    def _check_input_bool(self, value, name):
        """Проверка входных логических аргументов """

    @abstractmethod
    def _compare_with_limit(self, param):
        """Проверка предельных значений входных аргументов"""

    # оптическая сила линзы - D
    @abstractmethod
    def get_optical_power(self):
        """Вычисление оптической силы линзы"""

    # увеличение линзы - Г
    @abstractmethod
    def get_lens_enlargement(self):
        """Вычисление увеличения линзы"""

    # фокусное расстояние линзы - F
    @abstractmethod
    def get__focal_length(self):
        """Фокальное расстояние линзы"""

    # расстояние от линзы до предмета - d
    @abstractmethod
    def get__dist_subject(self):
        """Расстояние от линзы до объекта"""

    # расстояние от линзы до изображения - f
    @abstractmethod
    def get__dist_image(self):
        """Расстояние от линзы до предмета"""

    @abstractmethod
    def display_graphic(self):
        """Отображение графика"""

    @abstractmethod
    def default_axis(self):
        """Отображение осей"""

    @abstractmethod
    def build_rays(self):
        """Отображение лучей"""

    @abstractmethod
    def build_graph(self):
        """Метод, который нужно вызвать для постройки и отображения графика"""

    @abstractmethod
    def build_arrow(self, x1, x2, y1, y2, color="g", label="Изображение"):
        """Построение стрелок"""

    @abstractmethod
    def build_object(self):
        """Метод построения объекта"""
