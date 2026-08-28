import colorsys
import numpy
import colour

class Colour:
    def __init__(self, hexCode):
        if not hexCode.startswith("#"):
            hexCode = '#' + hexCode
        if not self.isValid(hexCode):
            raise ValueError("tried to create a colour with faulty hexdecimal")
        self.hex = hexCode
        # Hexcode to RGB conversion
        r = int(hexCode[1:3],16)
        g = int(hexCode[3:5],16)
        b = int(hexCode[5:7],16)
        self.rgb = (r,g,b)
        # RGB to HSV conversion
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        self.hsv = (h*360,s*100,v*100)
        # CIELAB conversion
        self.lab = self.calculate_lab_values()

    def isValid(self, hexCode):
        if not isinstance (hexCode, str):
            return False
        if len(hexCode) != 7:
            return False
        try:
            int(hexCode[1:], 16)
            return True
        except ValueError:
            return False

    def calculate_lab_values(self):
        rgb = numpy.array(self.rgb) / 255
        sRGB_space = colour.RGB_COLOURSPACES["sRGB"]
        xyz = colour.RGB_to_XYZ(rgb, colourspace=sRGB_space)
        lab = colour.XYZ_to_Lab(xyz,illuminant=sRGB_space.whitepoint)
        return (float(lab[0]), float(lab[1]), float(lab[2])
    )
