from models.Graph import Graph
import matplotlib.pyplot as plt


class BiconcaveGraph(Graph):
    def display_graphic(self, dist_image, dist_subject, focal_length, height_subject, height_image, is_real_image):
        self.default_axis(dist_subject, dist_image, focal_length, height_subject, is_real_image)
        self.build_subject(dist_subject, height_subject)
        self.build_rays(dist_subject, dist_image, focal_length, height_subject, height_image, is_real_image)
        plt.legend(loc='lower right', shadow=True, fontsize='x-large')
        plt.show()

    def default_axis(self, dist_subject, dist_image, focal_length, height_subject, is_real_image):
        plt.plot([(-1) * dist_subject - 5, focal_length + 5], [0, 0], "black")  # X
        plt.plot([0, 0], [abs(height_subject) + 3, (-1) * abs(height_subject) - 3], "black")  # Y
        plt.plot([-0.5, 0, 0.5],
                 [abs(height_subject) + 4, abs(height_subject) + 3, abs(height_subject) + 4],
                 "black")
        plt.plot([-0.5, 0, 0.5],
                 [-abs(height_subject) - 4, -abs(height_subject) - 3, -abs(height_subject) - 4],
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
        y1 = height_subject
        y2 = height_image
        if height_subject != 0:
            plt.plot([(-1) * dist_subject, x1, 3],  # parallel_x
                     [height_subject, y1,
                      self.calculate_coordinate((-1) * focal_length, (-1) * dist_image, 0,
                                                height_image,
                                                3)], "blue")

            plt.plot([(-1) * focal_length, 0],
                     [0, height_subject], "--b")

            plt.plot([(-1) * focal_length, (-1) * focal_length],
                     [(-1) * height_subject - 1, height_subject + 1], "--r")

            plt.plot([(-1) * dist_subject, 0, 3],  # line_focus
                     [height_subject, 0,
                      self.calculate_coordinate(0, (-1) * dist_subject, 0, height_subject, 3)], "blue")

            self.build_arrow((-1) * dist_image, (-1) * dist_image, 0, y2, "--g")  # line_image
            plt.xlim((-1) * dist_subject + dist_image - 5, focal_length + 5)
        else:
            random_height = 5
            plt.plot([(-1) * dist_subject, x1, 3],  # random ray
                     [height_subject, 5,
                      self.calculate_coordinate((-1) * dist_image, 0, 0, random_height, 3)], "blue")

            plt.plot([0, (-1) * focal_length, 0],
                     [random_height,
                      self.calculate_coordinate(0, (-1) * dist_image, random_height, 0,
                                                (-1) * focal_length),
                      0], "--b")

            plt.plot([(-1) * focal_length, (-1) * focal_length],
                     [(-1) * height_subject - 5, height_subject + 5], "--r")

            plt.plot([(-1) * dist_subject, 0, 3],  # line_focus
                     [height_subject, 0,
                      self.calculate_coordinate(0, (-1) * dist_subject, 0, height_subject, 3)],
                     "blue")

            plt.plot([(-1) * dist_image, (-1) * dist_image], [0, 0], "mo", label="Изображение")
            plt.xlim((-1) * dist_subject + dist_image - 5, focal_length + 5)
