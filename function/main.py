from function.OpticBuilder import OpticalBuilder
from function.RefractionLightClass import RefractionLightClass

if __name__ == "__main__":
    r = RefractionLightClass()
    r.build_graph(25, 1, 2.3)

    # r = RefractionLightClass()
    # r.build_graph(30, "water", "air")

    x = OpticalBuilder(dist_subject=10, focal_length=5, height_subject=3, biconcave=True)
    x.execute()
