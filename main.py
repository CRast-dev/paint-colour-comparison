
from src.colour import Colour


def main():
    print("Paint Color Analyzer")
    print("Project initialized successfully.")
    testcolour = Colour("#C04040","","")
    print("Test Colour Output: " + testcolour.hex)


if __name__ == "__main__":
    main()