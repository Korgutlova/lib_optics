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

        self._check_input_numbers(dist_subject, "dist_subject")
        self._check_input_numbers(dist_image, "dist_image")
        self._check_input_numbers(focal_length, "focal_length")
        self._check_input_numbers(height_subject, "height_subject")
        self._check_input_numbers(height_image, "height_image")

        self._real_subject = real_subject
        self._real_image = real_image
        self._dist_subject = dist_subject
        self._dist_image = dist_image
        self._focal_length = focal_length
        self._height_subject = height_subject
        self._height_image = height_image

    def __str__(self):
        """Строковое представление объекта линзы"""
        return "F - %s\nf - %s\nd - %s" % (self._focal_length, self._dist_image, self._dist_subject)

    @property
    def real_subject(self):
        """
        Реален ли объект

        real_subject: bool
            Является объект реальным или нет
        """
        return self._real_subject

    @real_subject.setter
    def real_subject(self, value):
        """
        Добавление реальности объекта

        Parameters
        ----------
        :param value: bool
            Является объект реальным или нет

        """
        self._check_input_bool(value, "real_subject")
        self._real_subject = value

    @property
    def real_image(self):
        """
        Реально ли изображение

        real_image: bool
            Является изображение реальным или нет
        """
        return self._real_image

    @real_image.setter
    def real_image(self, value):
        """
        Добавление реальности изображения

        Parameters
        ----------

        :param value: bool
            Является изображение реальным или нет
        """
        self._check_input_bool(value, "real_image")
        self._real_image = value

    @property
    def dist_subject(self):
        """
        dist_image: float
            Расстояние от линзы до объекта
        """
        return self._dist_subject

    @dist_subject.setter
    def dist_subject(self, value):
        """
        Добавление расстояния от линзы до объекта

        Parameters
        ----------
        :param value: float
            Расстояние от линзы до объекта
        """
        self._check_input_numbers(value, "dist_subject")
        self._dist_subject = value

    @property
    def dist_image(self):
        """
        dist_image: float
            Расстояние от линзы до изображения
        """
        return self._dist_image

    @dist_image.setter
    def dist_image(self, value):
        """
        Добавление расстояния от линзы до изображения

        Parameters
        ----------
        :param value: float
            Расстояние от линзы до изображения
        """
        self._check_input_numbers(value, "dist_image")
        self._dist_image = value

    @property
    def focal_length(self):
        """
        focal_length: float
            фокусное расстояние линзы
        """
        return self._focal_length

    @focal_length.setter
    def focal_length(self, value):
        """
        Добавление фокусного расстояния линзы

        Parameters
        ----------

        :param value: float
            фокусное расстояние линзы
        """
        self._check_input_numbers(value, "focal_length")
        self._focal_length = value

    @property
    def height_subject(self):
        """
        height_subject: float
            Высота предмета
        """
        return self._height_subject

    @height_subject.setter
    def height_subject(self, value):
        """
        Добавление высоты объекта

        Parameters
        ----------

        :param value: float
            Высота объекта
        """
        self._check_input_numbers(value, "height_subject")
        self._height_subject = value

    @property
    def height_image(self):
        """
        height_image: float
            Высота изображения
        """
        return self._height_image

    @height_image.setter
    def height_image(self, value):
        """
        Добавление высоты изображения

        Parameters
        ----------

        :param value: float
            Высота изображения
        """
        self._check_input_numbers(value, "height_image")
        self._height_image = value

    def _check_input_numbers(self, value, name):
        """
        Проверка входных числовых аргументов

        Parameters
        ----------

        :param value: float
            Значение числового аргумента
        :param name: str
            Строковое имя числового аргумента

        :raises ошибка InvalidArgumentForLens, если в качестве value передано не числовое значение или если value
            выходит за пределы допустимых значений
        """
        if value is not None and not isinstance(value, numbers.Number):
            raise errors.InvalidArgumentForLens(self._pattern_invalid_argument % (value, name, "Number"))

        if not self._is_within_limits(value):
            raise errors.InvalidArgumentForLens(self._pattern_over_limit_argument % (value, name))

    def _check_input_bool(self, value, name):
        """
        Проверка входных логических аргументов

        Parameters
        ----------

        :param value: bool
            Значение логического аргумента
        :param name: str
            Строковое имя логического аргумента

        :raises ошибка InvalidArgumentForLens, если в качестве value передано не логическое значение
        """
        if value is not None and not isinstance(value, bool):
            raise errors.InvalidArgumentForLens(self._pattern_invalid_argument % (value, name, "bool"))

    def _is_within_limits(self, param):
        """
        Проверка предельных значений входных аргументов

        Parameters
        ----------

        :param param: float
            Значение числового параметра

        :returns True, если param находится в пределах допустимых значений, иначе False
        """
        if param is None:
            return True
        return self._max_limit_value >= param >= self._min_limit_vale

    def check_not_none_for_F(self):
        """
        Проверка, возможно ли вычислить фокусное расстояние линзы

        :returns True, если значения, необходимые для вычисления фокускного расстояния, а именно расстояние от линзы
            до предмета и растояние от линзы до изображения, не None, иначе False
        """
        return self._dist_subject is not None and self._dist_image is not None

    def check_not_none_for_d(self):
        """
        Проверка, возможно ли вычислить расстояние от линзы до предмета

        :returns True, если значения, необходимые для вычисления расстояния от линзы до предмета, а именно фокусное
            расстояние линзы и растояние от линзы до изображения, не None, иначе False
        """
        return self._focal_length is not None and self._dist_image is not None

    def check_not_none_for_f(self):
        """
        Проверка, возможно ли вычислить расстояние от линзы до изображения

        :returns True, если значения, необходимые для вычисления расстояния от линзы до изображения, а именно
            фокусное расстояние линзы и растояние от линзы до объекта, не None, иначе False
        """
        return self._focal_length is not None and self._dist_subject is not None

    def get_optical_power(self):
        """
        Метод, вычисляющий оптическую силу линзы

        :returns оптическую силу линзы, если фокусное расстояние не None, иначе None
        """
        return 1 / self._focal_length if self._focal_length is not None else None

    def get_lens_enlargement(self):
        """
        Метод, вычисляющий увеличение линзы

        :returns увеличение линзы, если расстояние от линзы до изображения и расстояние от линзы до объекта не None,
            иначе None
        """
        return self._dist_image / self._dist_subject \
            if self._dist_image is not None and self._dist_subject is not None else None

    @abstractmethod
    def get__focal_length(self):
        """
        Метод, вычисляющий фокусное расстояние линзы

        :returns фокусное расстояние линзы
        """

    @abstractmethod
    def get__dist_subject(self):
        """
        Метод, вычисляющий расстояние от линзы до объекта

        :returns расстояние от линзы до объекта
        """

    @abstractmethod
    def get__dist_image(self):
        """
        Метод, вычисляющий расстояние от линзы до изображения

        :returns расстояние от линзы до изображения
        """

    @abstractmethod
    def display_graphic(self):
        """Метод, который нужно вызвать для построения и отображения графика"""


class LensInterface(ABC):

    @abstractmethod
    def __str__(self):
        """Строковое отображение"""

    @abstractmethod
    def _check_input_numbers(self, value, name):
        """
        Проверка входных числовых аргументов

        Parameters
        ----------

        value: float
            Значение числового аргумента
        name: str
            Строковое имя числового аргумента
        """

    @abstractmethod
    def _check_input_bool(self, value, name):
        """
        Проверка входных логических аргументов

        Parameters
        ----------

        value: bool
            Значение логического аргумента
        name: str
            Строковое имя логического аргумента
        """

    @abstractmethod
    def _is_within_limits(self, param):
        """
        Проверка предельных значений входных аргументов

        Parameters
        ----------

        param: float
            Значение числового параметра

        :returns True, если param находится в пределах допустимых значений, иначе False
        """

    @abstractmethod
    def get_optical_power(self):
        """
        Метод, вычисляющий оптическую силу линзы

        :returns оптическую силу линзы, если фокусное расстояние не None, иначе None
        """

    @abstractmethod
    def get_lens_enlargement(self):
        """
        Метод, вычисляющий увеличение линзы

        :returns увеличение линзы, если расстояние от линзы до изображения и расстояние от линзы до объекта не None,
            иначе None
        """

    @abstractmethod
    def get__focal_length(self):
        """
        Метод, вычисляющий фокусное расстояние линзы

        :returns фокусное расстояние линзы
        """

    @abstractmethod
    def get__dist_subject(self):
        """
        Метод, вычисляющий расстояние от линзы до предмета

        :returns расстояние от линзы до предмета
        """

    @abstractmethod
    def get__dist_image(self):
        """
        Метод, вычисляющий расстояние от линзы до изображения

        :returns расстояние от линзы до изображения
        """

    @abstractmethod
    def display_graphic(self):
        """Метод, который нужно вызвать для построения и отображения графика"""
