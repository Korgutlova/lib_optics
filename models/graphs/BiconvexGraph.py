from models.graphs.LensGraph import LensGraph
import matplotlib.pyplot as plt


class BiconvexGraph(LensGraph):
    """Класс для графиков с двояковогнутыми собирающими линзами"""

    def build_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        """Построение осей координат"""
        x_axes = dist_image if dist_image is not None else focal_length
        if is_real_image:
            plt.plot([(-1) * dist_subject - 5, x_axes + 5], [0, 0], self._axes_color)
        else:
            plt.plot([(-1) * dist_subject + x_axes - 5, focal_length + 5], [0, 0], self._axes_color)

        plt.plot([0, 0], [abs(height_subject) + 3, (-1) * abs(height_subject) - 3], self._axes_color)
        plt.plot([-0.5, 0, 0.5], [abs(height_subject) + 2, abs(height_subject) + 3, abs(height_subject) + 2],
                 self._axes_color)
        plt.plot([-0.5, 0, 0.5], [-abs(height_subject) - 2, -abs(height_subject) - 3, -abs(height_subject) - 2],
                 self._axes_color)
        plt.annotate("Линза", xy=(0.7, height_subject + 2))
        plt.axis('equal')
        self.build_focus(focal_length)

    def build_rays(self, dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image):
        """Построение лучей"""
        x1 = 0
        x2 = focal_length
        y1 = height_subject
        y2 = 0
        y3 = height_image
        if is_real_image:
            if dist_image is None or height_image is None:
                plt.plot([(-1) * dist_subject, x1, 1.5 * x2],  # parallel_x
                         [height_subject, y1, self.calculate_coordinate(x1, x2, y1, y2, x=1.5 * x2)], self._rays_color)

                plt.plot([(-1) * dist_subject, 1.5 * x2],  # line_focus
                         [height_subject, self.calculate_coordinate(0, x2, 0, -height_subject, x=1.5 * x2)],
                         self._rays_color)
            else:
                plt.plot([(-1) * dist_subject, x1, dist_image], [height_subject, y1, (-1) * y3], self._rays_color)

                plt.plot([(-1) * dist_subject, 0, dist_image],  # line_focus
                         [height_subject, (-1) * y3, (-1) * y3], self._rays_color)
                self.build_arrow(dist_image, dist_image, 0, (-1) * y3, self._subject_dash, self._image_label)
        else:
            plt.plot([(-1) * dist_subject, x1, x2], [height_subject, y1, y2], self._rays_color)
            plt.plot([x1, dist_image], [y1, y3], self._rays_dash)

            plt.plot([0, (-1) * dist_subject], [0, height_subject], self._rays_color)

            plt.plot([(-1) * dist_subject, dist_image], [height_subject, y3], self._rays_dash)

            self.build_arrow(dist_image, dist_image, 0, y3, self._subject_dash, self._image_label)

        if dist_image is None:
            plt.xlim((-1) * focal_length - 5, focal_length + 5)
        else:
            if is_real_image:
                plt.xlim((-1) * dist_subject - 5, dist_image + 5)
            else:
                plt.xlim((-1) * dist_subject + dist_image - 5, focal_length + 5)
