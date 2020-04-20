from abc import ABC, abstractmethod

import numbers

from util import errors


class AbstractLens(ABC):
    """Абстрактный класс линзы, используется для создания дочерних классов-линз"""
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
        """Реальный ли предмет"""
        return self._real_subject

    @real_subject.setter
    def real_subject(self, value):
        """Сеттер реальности предмета"""
        self._check_input_bool(value, "real_subject")
        self._real_subject = value

    @property
    def real_image(self):
        """Реально ли изображение"""
        return self._real_image

    @real_image.setter
    def real_image(self, value):
        """Сеттер реальности изображения"""
        self._check_input_bool(value, "real_image")
        self._real_image = value

    @property
    def dist_subject(self):
        """Расстояние от линзы до предмета"""
        return self._dist_subject

    @dist_subject.setter
    def dist_subject(self, value):
        """Сеттер расстояния от линзы до предмета"""
        self._check_input_numbers(value, "dist_subject")
        self._dist_subject = value

    @property
    def dist_image(self):
        """Расстояние от линзы до изображения"""
        return self._dist_image

    @dist_image.setter
    def dist_image(self, value):
        """Сеттер расстояния от линзы до изображения"""
        self._check_input_numbers(value, "dist_image")
        self._dist_image = value

    @property
    def focal_length(self):
        """Фокальное расстояние линзы"""
        return self._focal_length

    @focal_length.setter
    def focal_length(self, value):
        """Сеттер фокального расстояния линзы"""
        self._check_input_numbers(value, "focal_length")
        self._focal_length = value

    @property
    def height_subject(self):
        """Высота предмета"""
        return self._height_subject

    @height_subject.setter
    def height_subject(self, value):
        """Сеттер высоты предмета"""
        self._check_input_numbers(value, "height_subject")
        self._height_subject = value

    @property
    def height_image(self):
        """Высота изображения"""
        return self._height_image

    @height_image.setter
    def height_image(self, value):
        """Сеттер высоты изображения"""
        self._check_input_numbers(value, "height_image")
        self._height_image = value

    def _check_input_numbers(self, value, name):
        """Проверка входных числовых аргументов"""
        if value is not None and not isinstance(value, numbers.Number):
            raise errors.InvalidArgumentForLens(self._pattern_invalid_argument % (value, name, "Number"))

        if not self._compare_with_limit(value):
            raise errors.InvalidArgumentForLens(self._pattern_over_limit_argument % (value, name))

    def _check_input_bool(self, value, name):
        """Проверка входных логических аргументов"""
        if value is not None and not isinstance(value, bool):
            raise errors.InvalidArgumentForLens(self._pattern_invalid_argument % (value, name, "bool"))

    def _compare_with_limit(self, param):
        """Проверка предельных значений входных аргументов"""
        if param is None:
            return True
        return self._max_limit_value >= param >= self._min_limit_vale

    def check_not_none_for_F(self):
        """Проверка, подано ли на вход фокальное расстояние линзы"""
        return self._dist_subject is not None and self._dist_image is not None

    def check_not_none_for_d(self):
        """Проверка, подано ли на вход расстояние линзы от линзы до предмета"""
        return self._focal_length is not None and self._dist_image is not None

    def check_not_none_for_f(self):
        """Проверка, подано ли на вход расстояние линзы от линзы до изображения"""
        return self._focal_length is not None and self._dist_subject is not None

    def get_optical_power(self):
        """Метод, вычисляющий оптическую силу линзы"""
        return 1 / self._focal_length if self._focal_length is not None else None

    def get_lens_enlargement(self):
        """Метод, вычисляющий увеличение линзы"""
        return self._dist_image / self._dist_subject \
            if self._dist_image is not None and self._dist_subject is not None else None

    @abstractmethod
    def get__focal_length(self):
        """Фокальное расстояние линзы"""

    @abstractmethod
    def get__dist_subject(self):
        """Расстояние от линзы до объекта"""

    @abstractmethod
    def get__dist_image(self):
        """Расстояние от линзы до предмета"""

    @abstractmethod
    def display_graphic(self):
        """Метод, который нужно вызвать для постройки и отображения графика"""


class LensInterface(ABC):

    @abstractmethod
    def __str__(self):
        """Строковое отображение"""

    @abstractmethod
    def _check_input_numbers(self, value, name):
        """Проверка входных числовых аргументов"""

    @abstractmethod
    def _check_input_bool(self, value, name):
        """Проверка входных логических аргументов"""

    @abstractmethod
    def _compare_with_limit(self, param):
        """Проверка предельных значений входных аргументов"""

    @abstractmethod
    def get_optical_power(self):
        """Вычисление оптической силы линзы"""

    @abstractmethod
    def get_lens_enlargement(self):
        """Вычисление увеличения линзы"""

    @abstractmethod
    def get__focal_length(self):
        """Фокальное расстояние линзы"""

    @abstractmethod
    def get__dist_subject(self):
        """Расстояние от линзы до объекта"""

    @abstractmethod
    def get__dist_image(self):
        """Расстояние от линзы до предмета"""

    @abstractmethod
    def display_graphic(self):
        """Метод, который нужно вызвать для постройки и отображения графика"""
