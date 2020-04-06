from function.OpticBuilder import OpticalBuilder
from function.RefractionLightClass import RefractionLightClass

if __name__ == "__main__":
    r = RefractionLightClass()
    r.build_graph(25, 1, 2.3)

    # opt_build = OpticalBuilder()
    # opt_build.focal_length = 2
    # print(opt_build.get_optical_power())
    # print(opt_build)
    #
    # opt_build.height_subject = 5
    # opt_build.dist_subject = 3
    # opt_build.execute()