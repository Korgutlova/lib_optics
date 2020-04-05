import matplotlib.pyplot as plt


class OpticalBuilder:

    # http://fizmat.by/kursy/geom_optika/linzy

    def __init__(self):
        # d - distance from subject to lens - d
        self.dist_subject = None
        # f - distance from the subject image to the lens  - f
        self.dist_image = None
        # F - focal length F
        self.focal_length = None
        # [+/-] -  scattering lens / collecting lens
        self.lens_type = None
        # [+/-] - image is real
        self.real_image = None
        # [+/-] - subject is real
        self.real_subject = None
        # h - height of subject
        self.height_subject = None
        # h' - height of image
        self.height_image = None

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
        return self.dist_image * self.dist_subject / (self.dist_subject + self.dist_image) \
            if self.check_not_none_for_F() else None

    # расстояние от линзы до предмета - d
    def get_dist_subject(self):
        return self.focal_length * self.dist_image / (self.dist_image - self.focal_length) \
            if self.check_not_none_for_d() else None

    # расстояние от линзы до изображения - f
    def get_dist_image(self):
        return self.focal_length * self.dist_subject / (self.dist_subject - self.focal_length) \
            if self.check_not_none_for_f() else None

    # только действительных изображений
    def display_graphic(self):
        self.default_axis()
        self.build_object()
        self.build_rays()
        plt.show()

    def default_axis(self):
        X = plt.plot([(-1) * self.dist_subject - 5, self.dist_image + 5], [0, 0], "black")
        Y = plt.plot([0, 0], [self.height_subject + 1, (-1) * self.height_subject - 1], "black")
        plt.annotate("Линза", xy=(0, self.height_subject + 2))
        plt.axis('equal')
        frame = plt.gca()
        frame.axes.get_xaxis().set_ticks([])
        frame.axes.get_yaxis().set_ticks([])
        plt.plot([self.focal_length, self.focal_length], [-0.5, 0.5], "r")
        plt.plot([-self.focal_length, -self.focal_length], [-0.5, 0.5], "r")
        plt.annotate("F", xy=(self.focal_length, -1), color="r")
        plt.annotate("F", xy=(-self.focal_length, -1), color="r")

    def build_object(self):
        obj = plt.plot([(-1) * self.dist_subject, (-1) * self.dist_subject], [0, self.height_subject], "g")
        plt.annotate("Объект", xy=((-1) * self.dist_subject, 1))

    def build_rays(self):
        x1 = 0
        x2 = self.focal_length
        y1 = self.height_subject
        y2 = 0
        y3 = self.build_line_by_points(x1, x2, y1, y2, self.dist_image)
        parallel_x = plt.plot([(-1) * self.dist_subject, x1, x2, self.dist_image],
                              [self.height_subject, y1, y2, y3], "blue")

        line_focus = plt.plot([(-1) * self.dist_subject, (-1) * self.focal_length, 0, self.dist_image],
                              [self.height_subject, 0, y3, y3], "blue")

        line_image = plt.plot([self.dist_image, self.dist_image], [0, y3], "--g")
        plt.annotate("Изображение", xy=(self.dist_image, 1))

    def build_line_by_points(self, x1, x2, y1, y2, x=None, y=None):
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        if x is not None:
            return k * x + b
        return (y - b) / k

    def execute(self):
        if self.check_not_none_for_d():
            self.dist_subject = self.get_dist_subject()
        elif self.check_not_none_for_F():
            self.focal_length = self.get_focal_length()
        elif self.check_not_none_for_f():
            self.dist_image = self.get_dist_image()
        else:
            print("Заполните два из параметра f, d, F")
            return

        if self.dist_subject < self.focal_length:
            print("Для этой функции расстояние объекта до линзы должно быть больше чем фокусное расстояние")
            return

        if self.height_subject is None:
            print("Введите высоту предмета")
            return

        self.display_graphic()