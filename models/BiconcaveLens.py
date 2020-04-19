import matplotlib.pyplot as plt

from models.Lens import Lens


class BiconcaveLens(Lens):
    # фокусное расстояние линзы - F
    def get__focal_length(self):
        return self._dist_image * self._dist_subject / (self._dist_subject + self._dist_image) \
            if self.check_not_none_for_F() else None

    # расстояние от линзы до предмета - d
    def get__dist_subject(self):
        return self._focal_length * self._dist_image / (self._dist_image - self._focal_length) \
            if self.check_not_none_for_d() else None

    # расстояние от линзы до изображения - f
    def get__dist_image(self):
        return self._focal_length * self._dist_subject / (self._dist_subject + self._focal_length) \
            if self.check_not_none_for_f() else None

    def display_graphic(self):
        if self._dist_image is not None:
            self._height_image = self.calculate_coordinate(0, self._focal_length, self._height_subject, 0,
                                                           self._dist_image)
        else:
            self._height_image = 0
        self.default_axis()
        self.build_object()
        self.build_rays()
        plt.legend(loc='lower right', shadow=True, fontsize='x-large')
        plt.show()

    def default_axis(self):
        plt.plot([(-1) * self._dist_subject - 5, self._focal_length + 5], [0, 0], "black")  # X
        plt.plot([0, 0], [abs(self._height_subject) + 3, (-1) * abs(self._height_subject) - 3], "black")  # Y
        plt.plot([-0.5, 0, 0.5],
                 [abs(self._height_subject) + 4, abs(self._height_subject) + 3, abs(self._height_subject) + 4],
                 "black")
        plt.plot([-0.5, 0, 0.5],
                 [-abs(self._height_subject) - 4, -abs(self._height_subject) - 3, -abs(self._height_subject) - 4],
                 "black")
        plt.annotate("Линза", xy=(0, self._height_subject + 2))
        plt.axis('equal')
        plt.plot([self._focal_length, self._focal_length], [-0.5, 0.5], "r", label="Фокус")
        plt.plot([-self._focal_length, -self._focal_length], [-0.5, 0.5], "r")

    def build_rays(self):
        x1 = 0
        x2 = self._focal_length
        y1 = self._height_subject
        y2 = 0
        y3 = self._height_image
        if self._height_subject != 0:
            plt.plot([(-1) * self._dist_subject, x1, 3],  # parallel_x
                     [self._height_subject, y1,
                      self.calculate_coordinate((-1) * self._focal_length, (-1) * self._dist_image, 0,
                                                self._height_image,
                                                3)], "blue")

            plt.plot([(-1) * self._focal_length, 0],
                     [0, self._height_subject], "--b")

            plt.plot([(-1) * self._focal_length, (-1) * self._focal_length],
                     [(-1) * self._height_subject - 1, self._height_subject + 1], "--r")

            plt.plot([(-1) * self._dist_subject, 0, 3],  # line_focus
                     [self._height_subject, 0,
                      self.calculate_coordinate(0, (-1) * self._dist_subject, 0, self._height_subject, 3)], "blue")

            self.build_arrow((-1) * self._dist_image, (-1) * self._dist_image, 0, y3, "--g")  # line_image
            plt.xlim((-1) * self._dist_subject + self._dist_image - 5, self._focal_length + 5)
        else:
            random_height = 5
            plt.plot([(-1) * self._dist_subject, x1, 3],  # random ray
                     [self._height_subject, 5,
                      self.calculate_coordinate((-1) * self._dist_image, 0, 0, random_height, 3)], "blue")

            plt.plot([0, (-1) * self._focal_length, 0],
                     [random_height,
                      self.calculate_coordinate(0, (-1) * self._dist_image, random_height, 0,
                                                (-1) * self._focal_length),
                      0], "--b")

            plt.plot([(-1) * self._focal_length, (-1) * self._focal_length],
                     [(-1) * self._height_subject - 5, self._height_subject + 5], "--r")

            plt.plot([(-1) * self._dist_subject, 0, 3],  # line_focus
                     [self._height_subject, 0,
                      self.calculate_coordinate(0, (-1) * self._dist_subject, 0, self._height_subject, 3)],
                     "blue")

            plt.plot([(-1) * self._dist_image, (-1) * self._dist_image], [0, 0], "mo", label="Изображение")
            plt.xlim((-1) * self._dist_subject + self._dist_image - 5, self._focal_length + 5)

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

        self._real_image = False

        if self._height_subject is None:
            print("Введите высоту предмета")
            return

        self.display_graphic()
