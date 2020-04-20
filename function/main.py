from models.RefractionLightClass import RefractionLightClass
from models.lenses.BiconcaveLens import BiconcaveLens
from models.lenses.BiconvexLens import BiconvexLens

if __name__ == "__main__":
    # преломление света
    # r = RefractionLightClass()
    # r.set_refractive_indexes("file.csv")
    # r.build_graph(40, 1, "тестовый")

    # отражение света
    r = RefractionLightClass()
    r.build_graph(28.1, 'water', 1)
    #
    # точка и рассеивающая линза
    # x = BiconcaveLens(dist_subject=10, focal_length=5, height_subject=0)
    # # пример с валидацией
    # # x.dist_image = -10
    # x.display_graphic()
    #
    # # предмет и рассеивающая линза
    # x = BiconcaveLens(dist_subject=15, focal_length=10, height_subject=10)
    # x.display_graphic()
    #
    # # предмет на фокусном расстоянии и собирательная линза
    # x = BiconvexLens(dist_subject=10, focal_length=10, height_subject=5)
    # x.display_graphic()
    #
    # # предмет на фокусном расстоянии и собирательная линза
    # x = BiconvexLens(dist_subject=15, focal_length=8, height_subject=5)
    # x.display_graphic()
    #
    # # предмет внутри фокуса собирательной линзы
    # x = BiconvexLens(dist_subject=4, focal_length=5, height_subject=5)
    # # пример со сменой цвета
    # x.graph.image_color = "k"
    # x.graph.rays_color = "c"
    # x.display_graphic()
