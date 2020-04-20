from models.graphs.BiconcaveGraph import BiconcaveGraph
from models.lenses.AbstractLens import AbstractLens, LensInterface


class BiconcaveLens(AbstractLens, LensInterface):
    """Класс двояковогнутой рассеивающей линзы"""
    graph = BiconcaveGraph()

    def get__focal_length(self):
        """Фокальное расстояние двояковогнутой рассеивающей линзы"""
        return self._dist_image * self._dist_subject / (self._dist_subject + self._dist_image) \
            if self.check_not_none_for_F() else None

    def get__dist_subject(self):
        """Расстояние от двояковогнутой рассеивающей линзы до объекта"""
        return self._focal_length * self._dist_image / (self._dist_image - self._focal_length) \
            if self.check_not_none_for_d() else None

    def get__dist_image(self):
        """Расстояние от двояковогнутой рассеивающей линзы до изображения"""
        return self._focal_length * self._dist_subject / (self._dist_subject + self._focal_length) \
            if self.check_not_none_for_f() else None

    def display_graphic(self):
        """Метод, который нужно вызвать для постройки и отображения графика"""
        if self.check_not_none_for_d():
            self._dist_subject = self.get__dist_subject()
        elif self.check_not_none_for_F():
            self._focal_length = self.get__focal_length()
        elif self.check_not_none_for_f():
            self._dist_image = self.get__dist_image()
        else:
            print("Заполните два из параметра f, d, F")
            return

        self._real_image = False

        if self._height_subject is None:
            print("Введите высоту предмета")
            return

        if self._dist_image is not None:
            self._height_image = self.graph.calculate_coordinate(0, self._focal_length, self._height_subject, 0,
                                                                 self._dist_image)
        else:
            self._height_image = 0

        self.graph.build_graph(self._dist_image, self._dist_subject, self._focal_length, self._height_subject,
                               self._height_image, self._real_image)
