
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
    print("Euclidian distance: ", rgb_euclidian_distance)


def calculate_rgb_euclidian_dist(colour1, colour2):
    r_component = (colour1.rgb[0] - colour2.rgb[0])**2
    g_component = (colour1.rgb[1] - colour2.rgb[1])**2
    b_component = (colour1.rgb[2] - colour2.rgb[2])**2
    return math.sqrt(r_component + g_component + b_component)



if __name__ == "__main__":
    main()