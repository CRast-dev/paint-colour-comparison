
from src.colour import Colour


def main():
    print("####################### Paint Color Analyzer #######################")
    try:
        testcolour = Colour("#C04040")
        print(testcolour.hex)
        print(testcolour.rgb)
        print(testcolour.hsv)
        print("Parsed the colour correctly")
    except ValueError as error:
        print("faulty colour generation: ", error)
    


if __name__ == "__main__":
    main()