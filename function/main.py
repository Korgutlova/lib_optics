from function.OpticBuilder import OpticalBuilder
from function.RefractionLightClass import RefractionLightClass

if __name__ == "__main__":
    # r = RefractionLightClass()
    # r.build_graph(42, "water", "air")

    x = OpticalBuilder(dist_subject=5, dist_image=10, height_subject=3)
    x.execute()
