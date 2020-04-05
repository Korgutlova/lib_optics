from function.OpticBuilder import OpticalBuilder
from function.RefractionLightClass import RefractionLightClass

if __name__ == "__main__":
    r = RefractionLightClass()
    print(r.get_angle_refraction(30, "water", "air"))
    # r.get_refractive_index("test")

    r.build_graph(30, 1, "air")