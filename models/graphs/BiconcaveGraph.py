from models.graphs.LensGraph import LensGraph
import matplotlib.pyplot as plt


class BiconcaveGraph(LensGraph):
    """Класс для графиков с двояковыпуклыми рассеивающими линзами"""

    def build_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        """Построение осей координат"""
        plt.plot([(-1) * dist_subject - 5, focal_length + 5], [0, 0], self._axes_color)
        plt.plot([0, 0], [abs(height_subject) + 3, (-1) * abs(height_subject) - 3], self._axes_color)
        plt.plot([-0.5, 0, 0.5], [abs(height_subject) + 4, abs(height_subject) + 3, abs(height_subject) + 4],
                 self._axes_color)
        plt.plot([-0.5, 0, 0.5], [-abs(height_subject) - 4, -abs(height_subject) - 3, -abs(height_subject) - 4],
                 self._axes_color)
        plt.annotate("Линза", xy=(0.5, height_subject + 2))
        plt.axis('equal')
        self.build_focus(focal_length)

    def build_rays(self, dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image):
        """Построение лучей"""
        x1 = 0
        y1 = height_subject
        y2 = height_image
        if height_subject != 0:
            plt.plot([(-1) * dist_subject, x1, 3],  # parallel_x
                     [height_subject, y1,
                      self.calculate_coordinate((-1) * focal_length, (-1) * dist_image, 0,
                                                height_image,
                                                3)], self._rays_color)

            plt.plot([(-1) * focal_length, 0], [0, height_subject], self._rays_dash)

            plt.plot([(-1) * focal_length, (-1) * focal_length], [(-1) * height_subject - 1, height_subject + 1],
                     self._focus_dash)

            plt.plot([(-1) * dist_subject, 0, 3],  # line_focus
                     [height_subject, 0,
                      self.calculate_coordinate(0, (-1) * dist_subject, 0, height_subject, 3)], self._rays_color)

            self.build_arrow((-1) * dist_image, (-1) * dist_image, 0, y2, self._subject_dash, self._image_label)
            plt.xlim((-1) * dist_subject + dist_image - 5, focal_length + 5)
        else:
            random_height = 5
            plt.plot([(-1) * dist_subject, x1, 3],  # random ray
                     [height_subject, 5,
                      self.calculate_coordinate((-1) * dist_image, 0, 0, random_height, 3)], self._rays_color)

            plt.plot([0, (-1) * focal_length, 0],
                     [random_height, self.calculate_coordinate(0, (-1) * dist_image, random_height, 0,
                                                               (-1) * focal_length), 0], self._rays_dash)

            plt.plot([(-1) * focal_length, (-1) * focal_length],
                     [(-1) * height_subject - 5, height_subject + 5], self._focus_dash)

            plt.plot([(-1) * dist_subject, 0, 3],  # line_focus
                     [height_subject, 0,
                      self.calculate_coordinate(0, (-1) * dist_subject, 0, height_subject, 3)],
                     self._rays_color)

            plt.plot([(-1) * dist_image, (-1) * dist_image], [0, 0], self._image_point, self._image_label)
            plt.xlim((-1) * dist_subject + dist_image - 5, focal_length + 5)
