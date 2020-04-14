import matplotlib.pyplot as plt


class Lens:

    # http://fizmat.by/kursy/geom_optika/linzy

    def __init__(self, dist_subject=None, dist_image=None, focal_length=None, real_image=None,
                 real_subject=None, height_subject=None, height_image=None):
        # d - distance from subject to lens - d
        self.dist_subject = dist_subject
        # f - distance from the subject image to the lens  - f
        self.dist_image = dist_image
        # F - focal length F
        self.focal_length = focal_length
        # [+/-] - image is real
        self.real_image = real_image
        # [+/-] - subject is real
        self.real_subject = real_subject
        # h - height of subject
        self.height_subject = height_subject
        # h' - height of image
        self.height_image = height_image

    def __str__(self):
        return "F - %s\nf - %s\nd - %s" % (self.focal_length, self.dist_image, self.dist_subject)

    def check_not_none_for_F(self):
        return self.dist_subject is not None and self.dist_image is not None

    def check_not_none_for_d(self):
        return self.focal_length is not None and self.dist_image is not None

    def check_not_none_for_f(self):
        return self.focal_length is not None and self.dist_subject is not None

    # оптическая сила линзы - D
    def get_optical_power(self):
        return 1 / self.focal_length if self.focal_length is not None else None

    # увеличение линзы - Г
    def get_lens_enlargement(self):
        return self.dist_image / self.dist_subject \
            if self.dist_image is not None and self.dist_subject is not None else None

    # фокусное расстояние линзы - F
    def get_focal_length(self):
        pass

    # расстояние от линзы до предмета - d
    def get_dist_subject(self):
        pass

    # расстояние от линзы до изображения - f
    def get_dist_image(self):
        pass

    def display_graphic(self):
        pass

    def build_arrow(self, x1, x2, y1, y2, color="g"):
        plt.plot([x1, x2], [y1, y2], color)  # Object
        plt.plot([x1, x1 - 0.05 * y2], [y2, 0.85 * y2], color)  # Arrow Left
        plt.plot([x1, x1 + 0.05 * y2], [y2, 0.85 * y2], color)  # Arrow Right

    def default_axis(self):
        pass

    def build_object(self):
        if self.height_subject != 0:
            self.build_arrow((-1) * self.dist_subject, (-1) * self.dist_subject, 0, self.height_subject, "g")
        else:
            plt.plot([(-1) * self.dist_subject, (-1) * self.dist_subject], [0, 0], "go")  # Object
        plt.annotate("Объект", xy=((-1) * self.dist_subject, 1))

    def build_rays(self):
        pass

    def calculate_coordinate(self, x1, x2, y1, y2, x=None, y=None):
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        if x is not None:
            return k * x + b
        if y is not None:
            return (y - b) / k
        return None

    def build_graph(self):
        pass


class BiconcaveLens(Lens):

    # фокусное расстояние линзы - F
    def get_focal_length(self):
        return self.dist_image * self.dist_subject / (self.dist_subject + self.dist_image) \
            if self.check_not_none_for_F() else None

    # расстояние от линзы до предмета - d
    def get_dist_subject(self):
        return self.focal_length * self.dist_image / (self.dist_image - self.focal_length) \
            if self.check_not_none_for_d() else None

    # расстояние от линзы до изображения - f
    def get_dist_image(self):
        return self.focal_length * self.dist_subject / (self.dist_subject + self.focal_length) \
            if self.check_not_none_for_f() else None

    def display_graphic(self):
        if self.dist_image is not None:
            self.height_image = self.calculate_coordinate(0, self.focal_length, self.height_subject, 0,
                                                            self.dist_image)
        else:
            self.height_image = 0
        self.default_axis()
        self.build_object()
        self.build_rays()
        plt.show()

    def default_axis(self):
        plt.plot([(-1) * self.dist_subject - 5, self.focal_length + 5], [0, 0], "black")  # X
        plt.plot([0, 0], [abs(self.height_subject) + 3, (-1) * abs(self.height_subject) - 3], "black")  # Y
        plt.plot([-0.5, 0, 0.5],
                 [abs(self.height_subject) + 4, abs(self.height_subject) + 3, abs(self.height_subject) + 4],
                 "black")
        plt.plot([-0.5, 0, 0.5],
                 [-abs(self.height_subject) - 4, -abs(self.height_subject) - 3, -abs(self.height_subject) - 4],
                 "black")
        plt.annotate("Линза", xy=(0, self.height_subject + 2))
        plt.axis('equal')
        plt.plot([self.focal_length, self.focal_length], [-0.5, 0.5], "r")
        plt.plot([-self.focal_length, -self.focal_length], [-0.5, 0.5], "r")
        plt.annotate("F", xy=(self.focal_length, -1), color="r")
        plt.annotate("F", xy=(-self.focal_length, -1), color="r")

    def build_rays(self):
        x1 = 0
        x2 = self.focal_length
        y1 = self.height_subject
        y2 = 0
        y3 = self.height_image
        if self.height_subject != 0:
            plt.plot([(-1) * self.dist_subject, x1, 3],  # parallel_x
                     [self.height_subject, y1, self.calculate_coordinate((-1) * self.focal_length, (-1) * self.dist_image, 0, self.height_image, 3)], "blue")

            plt.plot([(-1) * self.focal_length, 0],
                     [0, self.height_subject], "--b")

            plt.plot([(-1) * self.focal_length, (-1) * self.focal_length],
                     [(-1) * self.height_subject - 1, self.height_subject + 1], "--r")

            plt.plot([(-1) * self.dist_subject, 0, 3],  # line_focus
                     [self.height_subject, 0, self.calculate_coordinate(0, (-1) * self.dist_subject, 0, self.height_subject, 3)], "blue")

            self.build_arrow((-1) * self.dist_image, (-1) * self.dist_image, 0, y3, "--g")  # line_image
            plt.annotate("Изображение", xy=((-1) * self.dist_image, self.height_image * 0.5))
            plt.xlim((-1) * self.dist_subject + self.dist_image - 5, self.focal_length + 5)
        else:
            random_height = 5
            plt.plot([(-1) * self.dist_subject, x1, 3],  # random ray
                     [self.height_subject, 5,
                      self.calculate_coordinate((-1) * self.dist_image, 0, 0, random_height, 3)], "blue")

            plt.plot([0, (-1) * self.focal_length, 0],
                     [random_height, self.calculate_coordinate(0, (-1) * self.dist_image, random_height, 0, (-1) * self.focal_length), 0], "--b")

            plt.plot([(-1) * self.focal_length, (-1) * self.focal_length],
                     [(-1) * self.height_subject - 5, self.height_subject + 5], "--r")

            plt.plot([(-1) * self.dist_subject, 0, 3],  # line_focus
                     [self.height_subject, 0,
                      self.calculate_coordinate(0, (-1) * self.dist_subject, 0, self.height_subject, 3)],
                     "blue")

            plt.plot([(-1) * self.dist_image, (-1) * self.dist_image], [0, 0], "go")  # line_image
            plt.annotate("Изображение", xy=((-1) * self.dist_image, self.height_image * 0.5))
            plt.xlim((-1) * self.dist_subject + self.dist_image - 5, self.focal_length + 5)

    def build_graph(self):
        if self.check_not_none_for_d():
            self.dist_subject = self.get_dist_subject()
        elif self.check_not_none_for_F():
            self.focal_length = self.get_focal_length()
        elif self.check_not_none_for_f():
            self.dist_image = self.get_dist_image()
        else:
            print("Заполните два из параметра f, d, F")
            return

        self.real_image = False

        if self.height_subject is None:
            print("Введите высоту предмета")
            return

        self.display_graphic()


class BiconvexLens(Lens):

    # фокусное расстояние линзы - F
    def get_focal_length(self):
        return self.dist_image * self.dist_subject / (self.dist_subject - self.dist_image) \
            if self.check_not_none_for_F() else None

    # расстояние от линзы до предмета - d
    def get_dist_subject(self):
        return self.focal_length * self.dist_image / (self.focal_length - self.dist_image) \
            if self.check_not_none_for_d() else None

    # расстояние от линзы до изображения - f
    def get_dist_image(self):
        if self.dist_subject - self.focal_length != 0:
            return self.focal_length * self.dist_subject / (self.dist_subject - self.focal_length) \
                if self.check_not_none_for_f() else None
        else:
            return None

    def display_graphic(self):
        if self.dist_image is not None:
            self.height_image = self.calculate_coordinate(0, (-1) * self.dist_subject, 0,
                                                            self.height_subject, (-1) * self.dist_image)
        else:
            self.height_image = 0
        self.default_axis()
        self.build_object()
        self.build_rays()
        plt.show()

    def default_axis(self):
        x_axes = self.dist_image if self.dist_image is not None else self.focal_length
        if self.real_image:
            plt.plot([(-1) * self.dist_subject - 5, x_axes + 5], [0, 0], "black")  # X
        else:
            plt.plot([(-1) * self.dist_subject + x_axes - 5, self.focal_length + 5], [0, 0], "black")  # X

        plt.plot([0, 0], [abs(self.height_subject) + 3, (-1) * abs(self.height_subject) - 3], "black")  # Y
        plt.plot([-0.5, 0, 0.5],
                 [abs(self.height_subject) + 2, abs(self.height_subject) + 3, abs(self.height_subject) + 2],
                 "black")
        plt.plot([-0.5, 0, 0.5],
                 [-abs(self.height_subject) - 2, -abs(self.height_subject) - 3, -abs(self.height_subject) - 2],
                 "black")
        plt.annotate("Линза", xy=(0, self.height_subject + 2))
        plt.axis('equal')
        plt.plot([self.focal_length, self.focal_length], [-0.5, 0.5], "r")
        plt.plot([-self.focal_length, -self.focal_length], [-0.5, 0.5], "r")
        plt.annotate("F", xy=(self.focal_length, -1), color="r")
        plt.annotate("F", xy=(-self.focal_length, -1), color="r")

    def build_rays(self):
        x1 = 0
        x2 = self.focal_length
        y1 = self.height_subject
        y2 = 0
        y3 = self.height_image
        if self.real_image:
            if self.dist_image is None or self.height_image is None:
                plt.plot([(-1) * self.dist_subject, x1, 1.5 * x2],  # parallel_x
                         [self.height_subject, y1, self.calculate_coordinate(x1, x2, y1, y2, x=1.5 * x2)], "blue")

                plt.plot([(-1) * self.dist_subject, 1.5 * x2],  # line_focus
                         [self.height_subject, self.calculate_coordinate(0, x2, 0, -self.height_subject, x=1.5 * x2)], "blue")
            else:
                plt.plot([(-1) * self.dist_subject, x1, self.dist_image],  # parallel_x
                         [self.height_subject, y1, (-1) * y3], "blue")

                plt.plot([(-1) * self.dist_subject,  0, self.dist_image],  # line_focus
                         [self.height_subject, (-1) * y3, (-1) * y3], "blue")
                self.build_arrow(self.dist_image, self.dist_image, 0, (-1) * y3, "--g")  # line_image
                plt.annotate("Изображение", xy=(self.dist_image, self.height_image * 0.5))
        else:
            plt.plot([(-1) * self.dist_subject, x1, x2],  # parallel_x
                     [self.height_subject, y1, y2], "blue")
            plt.plot([x1, self.dist_image],  # parallel_x_image
                     [y1, y3], "--b")

            plt.plot([0, (-1) * self.dist_subject],  # line_focus
                     [0, self.height_subject], "blue")

            plt.plot([(-1) * self.dist_subject, self.dist_image],  # line_focus_image
                     [self.height_subject, y3], "--b")
            self.build_arrow(self.dist_image, self.dist_image, 0, y3, "--g")  # line_image
            plt.annotate("Изображение", xy=(self.dist_image, self.height_image * 0.5))

        if self.dist_image is None:
            plt.xlim((-1) * self.focal_length - 5, self.focal_length + 5)
        else:
            if self.real_image:
                plt.xlim((-1) * self.dist_subject - 5, self.dist_image + 5)
            else:
                plt.xlim((-1) * self.dist_subject + self.dist_image - 5, self.focal_length + 5)

    def build_graph(self):
        if self.check_not_none_for_d():
            self.dist_subject = self.get_dist_subject()
        elif self.check_not_none_for_F():
            self.focal_length = self.get_focal_length()
        elif self.check_not_none_for_f():
            self.dist_image = self.get_dist_image()
        else:
            print("Заполните два из параметра f, d, F")
            return

        self.real_image = not self.dist_subject < self.focal_length

        if self.height_subject is None:
            print("Введите высоту предмета")
            return

        self.display_graphic()
