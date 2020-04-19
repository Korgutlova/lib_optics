from models.BiconvexGraph import BiconvexGraph
from models.Lens import Lens, LensInterface


class BiconvexLens(Lens, LensInterface):

    graph = BiconvexGraph()

    # фокусное расстояние линзы - F
    def get__focal_length(self):
        return self._dist_image * self._dist_subject / (self._dist_subject - self._dist_image) \
            if self.check_not_none_for_F() else None

    # расстояние от линзы до предмета - d
    def get__dist_subject(self):
        return self._focal_length * self._dist_image / (self._focal_length - self._dist_image) \
            if self.check_not_none_for_d() else None

    # расстояние от линзы до изображения - f
    def get__dist_image(self):
        if self._dist_subject - self._focal_length != 0:
            return self._focal_length * self._dist_subject / (self._dist_subject - self._focal_length) \
                if self.check_not_none_for_f() else None
        else:
            return None

    def build_graph(self):
        if self.check_not_none_for_d():
            self._dist_subject = self.get__dist_subject()
        elif self.check_not_none_for_F():
            self._focal_length = self.get__focal_length()
        elif self.check_not_none_for_f():
            self._dist_image = self.get__dist_image()
        else:
            print("Заполните два из параметра f, d, F")
            return

        self._real_image = not self._dist_subject < self._focal_length

        if self._height_subject is None:
            print("Введите высоту предмета")
            return

        if self._dist_image is not None:
            self._height_image = self.graph.calculate_coordinate(0, (-1) * self._dist_subject, 0, self._height_subject,
                                                           (-1) * self._dist_image)
        else:
            self._height_image = 0

        self.graph.display_graphic(self._dist_image, self._dist_subject, self._focal_length, self._height_subject,
                                   self._height_image, self._real_image)
