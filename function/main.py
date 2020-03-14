from function.RefractionLightClass import RefractionLightClass

if __name__ == "__main__":
    r = RefractionLightClass()
    print(r.get_angle_refraction(30, "air", "water"))