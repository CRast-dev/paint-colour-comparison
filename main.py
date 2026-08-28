
from src.colour import Colour
import math

def main():
    print("####################### Paint Color Analyzer #######################")
    try:
        colour1 = Colour("#C04040")
        colour2 = Colour("#C11111")
    except ValueError as error:
        print("faulty colour generation: ", error)

    rgb_euclidian_distance = calculate_rgb_euclidian_dist(colour1,colour2)
    hsv_euclidian_distance = calculate_hsv_dist(colour1, colour2)
    cie76_distance = calculate_cie76_distance(colour1, colour2)
    print("Euclidian distance: ", rgb_euclidian_distance)
    print("HSV euclidian distance: ", hsv_euclidian_distance)
    print(f"Lab: {colour1.lab}")
    print("CIE76 distance: ", cie76_distance) 

def calculate_rgb_euclidian_dist(colour1, colour2):
    r_component = (colour1.rgb[0] - colour2.rgb[0])**2
    g_component = (colour1.rgb[1] - colour2.rgb[1])**2
    b_component = (colour1.rgb[2] - colour2.rgb[2])**2
    return math.sqrt(r_component + g_component + b_component)

def calculate_hsv_dist(colour1, colour2):
    h1_radian = math.radians(colour1.hsv[0])
    s1 = colour1.hsv[1] / 360.0
    v1 = colour1.hsv[2] / 360.0
    x1_component = math.cos(h1_radian) * s1 * v1
    y1_component = math.sin(h1_radian) * s1 * v1
    z1_component = v1

    h2_radian = math.radians(colour2.hsv[0])
    s2 = colour2.hsv[1] / 360.0
    v2 = colour2.hsv[2] / 360.0
    x2_component = math.cos(h2_radian) * s2 * v2
    y2_component = math.sin(h2_radian) * s2 * v2
    z2_component = v2

    return math.sqrt((x1_component-x2_component)**2 + (y1_component - y2_component)**2 + (z1_component - z2_component)**2)



def calculate_cie76_distance(colour1, colour2):
    l_component = colour1.lab[0] - colour2.lab[0]
    a_component = colour1.lab[1] - colour2.lab[1]
    b_component = colour1.lab[2] - colour2.lab[2]

    return math.sqrt(l_component **2 + a_component **2 + b_component **2)

if __name__ == "__main__":
    main()