from function.OpticBuilder import OpticalBuilder
from function.RefractionLightClass import RefractionLightClass

if __name__ == "__main__":
    r = RefractionLightClass()
    print(r.get_angle_refraction(30, "water", "air"))
    # r.get_refractive_index("test")

    opt_build = OpticalBuilder()
    opt_build.focal_length = 3
    print(opt_build.get_optical_power())
    print(opt_build)
