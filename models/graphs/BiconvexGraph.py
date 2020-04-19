from models.graphs.LensGraph import LensGraph
import matplotlib.pyplot as plt


class BiconvexGraph(LensGraph):
    def build_graph(self, dist_image, dist_subject, focal_length, height_subject, height_image, is_real_image):
        self.default_axis(dist_subject, dist_image, focal_length, height_subject, is_real_image)
        self.build_subject(dist_subject, height_subject)
        self.build_rays(dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image)
        plt.legend(loc='lower right', shadow=True, fontsize='x-large')
        plt.show()

    def default_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        x_axes = dist_image if dist_image is not None else focal_length
        if is_real_image:
            plt.plot([(-1) * dist_subject - 5, x_axes + 5], [0, 0], "black")  # X
        else:
            plt.plot([(-1) * dist_subject + x_axes - 5, focal_length + 5], [0, 0], "black")  # X

        plt.plot([0, 0], [abs(height_subject) + 3, (-1) * abs(height_subject) - 3], "black")  # Y
        plt.plot([-0.5, 0, 0.5],
                 [abs(height_subject) + 2, abs(height_subject) + 3, abs(height_subject) + 2],
                 "black")
        plt.plot([-0.5, 0, 0.5],
                 [-abs(height_subject) - 2, -abs(height_subject) - 3, -abs(height_subject) - 2],
                 "black")
        plt.annotate("Линза", xy=(0, height_subject + 2))
        plt.axis('equal')
        plt.plot([focal_length, focal_length], [-0.5, 0.5], "r", label="Фокус")
        plt.plot([-focal_length, -focal_length], [-0.5, 0.5], "r")

    def build_subject(self, dist_subject, height_subject):
        if height_subject != 0:
            self.build_arrow((-1) * dist_subject, (-1) * dist_subject, 0, height_subject,
                             label="Объект")
        else:
            plt.plot([(-1) * dist_subject, (-1) * dist_subject], [0, 0], "go", label="Объект")  # Object

    def build_arrow(self, x1, x2, y1, y2, color="g", label="Изображение"):
        plt.plot([x1, x2], [y1, y2], color, label=label)  # Object
        plt.plot([x1, x1 - 0.05 * y2], [y2, 0.85 * y2], color)  # Arrow Left
        plt.plot([x1, x1 + 0.05 * y2], [y2, 0.85 * y2], color)  # Arrow Right

    def build_rays(self, dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image):
        x1 = 0
        x2 = focal_length
        y1 = height_subject
        y2 = 0
        y3 = height_image
        if is_real_image:
            if dist_image is None or height_image is None:
                plt.plot([(-1) * dist_subject, x1, 1.5 * x2],  # parallel_x
                         [height_subject, y1, self.calculate_coordinate(x1, x2, y1, y2, x=1.5 * x2)], "blue")

                plt.plot([(-1) * dist_subject, 1.5 * x2],  # line_focus
                         [height_subject, self.calculate_coordinate(0, x2, 0, -height_subject, x=1.5 * x2)],
                         "blue")
            else:
                plt.plot([(-1) * dist_subject, x1, dist_image],  # parallel_x
                         [height_subject, y1, (-1) * y3], "blue")

                plt.plot([(-1) * dist_subject, 0, dist_image],  # line_focus
                         [height_subject, (-1) * y3, (-1) * y3], "blue")
                self.build_arrow(dist_image, dist_image, 0, (-1) * y3, "--g")  # line_image
        else:
            plt.plot([(-1) * dist_subject, x1, x2],  # parallel_x
                     [height_subject, y1, y2], "blue")
            plt.plot([x1, dist_image],  # parallel_x_image
                     [y1, y3], "--b")

            plt.plot([0, (-1) * dist_subject],  # line_focus
                     [0, height_subject], "blue")

            plt.plot([(-1) * dist_subject, dist_image],  # line_focus_image
                     [height_subject, y3], "--b")
            self.build_arrow(dist_image, dist_image, 0, y3, "--g")  # line_image

        if dist_image is None:
            plt.xlim((-1) * focal_length - 5, focal_length + 5)
        else:
            if is_real_image:
                plt.xlim((-1) * dist_subject - 5, dist_image + 5)
            else:
                plt.xlim((-1) * dist_subject + dist_image - 5, focal_length + 5)
