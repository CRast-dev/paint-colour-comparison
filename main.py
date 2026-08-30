from tests.comparison_test import testValidateCIEDE2000
from src.colour import Colour
from src.comparison import calculate_rgb_euclidian_dist
from src.comparison import calculate_hsv_dist
from src.comparison import calculate_cie76_distance
from src.comparison import calculate_ciede2000_distance

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
    cie2000_distance = calculate_ciede2000_distance(colour1, colour2)
    print("Euclidian distance: ", rgb_euclidian_distance)
    print("HSV euclidian distance: ", hsv_euclidian_distance)
    print(f"Lab: {colour1.lab}")
    print("CIEDE2000 distance: ", cie2000_distance)
    print("CIE76 distance: ", cie76_distance)
    print("###### Temp Test to save my sanity ######")
    testValidateCIEDE2000()



if __name__ == "__main__":
    main()