from models.RefractionLightClass import RefractionLightClass
from models.lenses.BiconcaveLens import BiconcaveLens
from models.lenses.BiconvexLens import BiconvexLens

if __name__ == "__main__":
    # преломление света
    r = RefractionLightClass()
    medium_one = "water"
    medium_two = "air"
    angle = 40
    print(r.get_angle_refraction(angle, medium_one, medium_two))
    r.build_graph(angle, medium_one, medium_two)

    # отражение света
    r = RefractionLightClass()
    r.build_graph(28.1, 'water', 'air')

    # точка и рассеивающая линза
    x = BiconcaveLens(dist_subject=10, focal_length=5, height_subject=0)
    print("Distance image from lens %s " % x.get__dist_image())
    x.display_graphic()

    # предмет и рассеивающая линза
    lens = BiconcaveLens(dist_subject=8, focal_length=5, height_subject=3)
    print(lens.get__dist_image())
    lens.display_graphic()

    # предмет на фокусном расстоянии и собирательная линза
    x = BiconvexLens(dist_subject=10, focal_length=10, height_subject=5)
    x.display_graphic()

    # предмет на фокусном расстоянии и собирательная линза
    x = BiconvexLens(dist_subject=15, focal_length=8, height_subject=5)
    x.display_graphic()

    # предмет внутри фокуса собирательной линзы
    x = BiconvexLens(dist_subject=4, focal_length=5, height_subject=5)
    x.display_graphic()
