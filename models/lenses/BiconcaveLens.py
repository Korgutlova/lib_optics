from models.graphs.BiconcaveGraph import BiconcaveGraph
from models.lenses.AbstractLens import AbstractLens, LensInterface
from util import errors


class BiconcaveLens(AbstractLens, LensInterface):
    """Класс двояковогнутой рассеивающей линзы"""
    graph = BiconcaveGraph()

    def get__focal_length(self):
        """
        Метод, вычисляющий фокусное расстояние линзы

        :returns фокусное расстояние линзы
        """
        return self._dist_image * self._dist_subject / (self._dist_subject + self._dist_image)

    def get__dist_subject(self):
        """
        Метод, вычисляющий расстояние от линзы до предмета

        :returns расстояние от линзы до предмета
        """
        return self._focal_length * self._dist_image / (self._dist_image - self._focal_length)

    def get__dist_image(self):
        """
        Метод, вычисляющий расстояние от линзы до изображения

        :returns расстояние от линзы до изображения
        """
        return self._focal_length * self._dist_subject / (self._dist_subject + self._focal_length)

    def display_graphic(self):
        """Метод для построения и отображения графика"""
        if self.check_not_none_for_d():
            self._dist_subject = self.get__dist_subject()
        elif self.check_not_none_for_F():
            self._focal_length = self.get__focal_length()
        elif self.check_not_none_for_f():
            self._dist_image = self.get__dist_image()
        else:
            raise errors.NotEnoughKnownValuesForLensGraphic("Недостаточно известных параметров. Заполните два из параметров: f, d, F")

        self._real_image = False

        if self._height_subject is None:
            raise errors.MissingObjectHeight("Необходимо ввести высоту объекта.")

        if self._dist_image is not None:
            self._height_image = self.graph.calculate_coordinate(0, self._focal_length, self._height_subject, 0,
                                                                 self._dist_image)
        else:
            self._height_image = 0

        self.graph.build_graph(self._dist_subject, self._dist_image,  self._height_subject, self._height_image,
                               self._focal_length, self._real_image)
