from function.OpticBuilder import OpticalBuilder
from function.RefractionLightClass import RefractionLightClass

if __name__ == "__main__":

    # преломление света
    r = RefractionLightClass()
    r.build_graph(40, "water", "air")

    # точка и рассеивающая линза
    x = OpticalBuilder(dist_subject=10, focal_length=5, height_subject=0, biconcave=True)
    x.execute()

    # предмет и рассеивающая линза
    x = OpticalBuilder(dist_subject=10, focal_length=5, height_subject=5, biconcave=True)
    x.execute()

    # предмет и собирательная линза
    x = OpticalBuilder(dist_subject=10, focal_length=5, height_subject=5, biconcave=False)
    x.execute()

    # предмет внутри фокуса собирательной линзы
    x = OpticalBuilder(dist_subject=4, focal_length=5, height_subject=5, biconcave=False)
    x.execute()
