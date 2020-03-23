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

    def check_not_none(self):
        return self.dist_subject is not None and self.dist_image is not None and self.lens_type is not None \
               and self.real_image is not None and self.real_subject is not None

    # оптическая сила линзы - D
    def get_optical_power(self):
        return 1 / self.focal_length if self.focal_length is not None else None

    # увеличение линзы - Г
    def get_lens_enlargement(self):
        return self.dist_image / self.dist_subject \
            if self.dist_image is not None and self.dist_subject is not None else None

    # фокусное расстояние линзы - F
    def get_focal_length(self):
        return self.lens_type * self.dist_image * self.dist_subject / \
               (self.real_subject * self.dist_subject + self.real_image * self.dist_image) \
            if self.check_not_none() else None
