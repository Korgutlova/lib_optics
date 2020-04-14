import matplotlib.pyplot as plt

from models.Lens import Lens


class BiconvexLens(Lens):

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

    def display_graphic(self):
        if self._dist_image is not None:
            self._height_image = self.calculate_coordinate(0, (-1) * self._dist_subject, 0,
                                                           self._height_subject, (-1) * self._dist_image)
        else:
            self._height_image = 0
        self.default_axis()
        self.build_object()
        self.build_rays()
        plt.show()

    def default_axis(self):
        x_axes = self._dist_image if self._dist_image is not None else self._focal_length
        if self._real_image:
            plt.plot([(-1) * self._dist_subject - 5, x_axes + 5], [0, 0], "black")  # X
        else:
            plt.plot([(-1) * self._dist_subject + x_axes - 5, self._focal_length + 5], [0, 0], "black")  # X

        plt.plot([0, 0], [abs(self._height_subject) + 3, (-1) * abs(self._height_subject) - 3], "black")  # Y
        plt.plot([-0.5, 0, 0.5],
                 [abs(self._height_subject) + 2, abs(self._height_subject) + 3, abs(self._height_subject) + 2],
                 "black")
        plt.plot([-0.5, 0, 0.5],
                 [-abs(self._height_subject) - 2, -abs(self._height_subject) - 3, -abs(self._height_subject) - 2],
                 "black")
        plt.annotate("Линза", xy=(0, self._height_subject + 2))
        plt.axis('equal')
        plt.plot([self._focal_length, self._focal_length], [-0.5, 0.5], "r")
        plt.plot([-self._focal_length, -self._focal_length], [-0.5, 0.5], "r")
        plt.annotate("F", xy=(self._focal_length, -1), color="r")
        plt.annotate("F", xy=(-self._focal_length, -1), color="r")

    def build_rays(self):
        x1 = 0
        x2 = self._focal_length
        y1 = self._height_subject
        y2 = 0
        y3 = self._height_image
        if self._real_image:
            if self._dist_image is None or self._height_image is None:
                plt.plot([(-1) * self._dist_subject, x1, 1.5 * x2],  # parallel_x
                         [self._height_subject, y1, self.calculate_coordinate(x1, x2, y1, y2, x=1.5 * x2)], "blue")

                plt.plot([(-1) * self._dist_subject, 1.5 * x2],  # line_focus
                         [self._height_subject, self.calculate_coordinate(0, x2, 0, -self._height_subject, x=1.5 * x2)],
                         "blue")
            else:
                plt.plot([(-1) * self._dist_subject, x1, self._dist_image],  # parallel_x
                         [self._height_subject, y1, (-1) * y3], "blue")

                plt.plot([(-1) * self._dist_subject, 0, self._dist_image],  # line_focus
                         [self._height_subject, (-1) * y3, (-1) * y3], "blue")
                self.build_arrow(self._dist_image, self._dist_image, 0, (-1) * y3, "--g")  # line_image
                plt.annotate("Изображение", xy=(self._dist_image, self._height_image * 0.5))
        else:
            plt.plot([(-1) * self._dist_subject, x1, x2],  # parallel_x
                     [self._height_subject, y1, y2], "blue")
            plt.plot([x1, self._dist_image],  # parallel_x_image
                     [y1, y3], "--b")

            plt.plot([0, (-1) * self._dist_subject],  # line_focus
                     [0, self._height_subject], "blue")

            plt.plot([(-1) * self._dist_subject, self._dist_image],  # line_focus_image
                     [self._height_subject, y3], "--b")
            self.build_arrow(self._dist_image, self._dist_image, 0, y3, "--g")  # line_image
            plt.annotate("Изображение", xy=(self._dist_image, self._height_image * 0.5))

        if self._dist_image is None:
            plt.xlim((-1) * self._focal_length - 5, self._focal_length + 5)
        else:
            if self._real_image:
                plt.xlim((-1) * self._dist_subject - 5, self._dist_image + 5)
            else:
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

        self._real_image = not self._dist_subject < self._focal_length

        if self._height_subject is None:
            print("Введите высоту предмета")
            return

        self.display_graphic()
