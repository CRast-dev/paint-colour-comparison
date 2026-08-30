from src.comparison import calculate_ciede2000_distance
from src.colour import Colour

def testValidateCIEDE2000():
    colour1 = Colour("#000000")
    colour2 = Colour("#000000")
    #force test case lab values
    colour1.lab = (50.0000, 2.6772, -79.7751)
    colour2.lab = (50.0000, 0.0000, -82.7485)
    result = calculate_ciede2000_distance(colour1, colour2)
    print(f"CIEDE2000 test result: {result:.4f}")
    print("Expected result: 2.0425")