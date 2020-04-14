from function.models import Lens, BiconcaveLens, BiconvexLens
from function.RefractionLightClass import RefractionLightClass

if __name__ == "__main__":
    # преломление света
    r = RefractionLightClass()
    r.build_graph(40, "water", "air")

    # отражение света
    r = RefractionLightClass()
    r.build_graph(28, 3, 1)

    # точка и рассеивающая линза
    x = BiconcaveLens(dist_subject=10, focal_length=5, height_subject=0)
    x.build_graph()

    # предмет и рассеивающая линза
    x = BiconcaveLens(dist_subject=15, focal_length=10, height_subject=10)
    x.build_graph()

    # предмет на фокусном расстоянии и собирательная линза
    x = BiconvexLens(dist_subject=10, focal_length=10, height_subject=5)
    x.build_graph()

    # предмет на фокусном расстоянии и собирательная линза
    x = BiconvexLens(dist_subject=15, focal_length=8, height_subject=5)
    x.build_graph()

    # предмет внутри фокуса собирательной линзы
    x = BiconvexLens(dist_subject=4, focal_length=5, height_subject=5)
    x.build_graph()
