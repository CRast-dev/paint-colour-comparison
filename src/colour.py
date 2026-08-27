import colorsys


class Colour:
    def __init__(self, hexCode):
        if not hexCode.startswith("#"):
            hexCode = '#' + hexCode
        if not self.isValid(hexCode):
            raise ValueError("tried to create a colour with faulty hexdecimal")
        self.hex = hexCode

        r = int(hexCode[1:3],16)
        g = int(hexCode[3:5],16)
        b = int(hexCode[5:7],16)
        self.rgb = (r,g,b)

        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        self.hsv = (h*360,s*360,v*360)

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