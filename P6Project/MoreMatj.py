from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, XYZColor

xyz = XYZColor(0.4, 0.2, 0.3)  # The XYZ color
rgb = convert_color(xyz, sRGBColor)  # Converts the XYZ color to sRGB
rgbb = rgb.get_value_tuple()  # Converts the color to a tuple
rgblist = []  # Empty list
for i in rgbb:  # For loop that converts tuple to floats and appends to a list
    x = float(i) * 255
    rgblist.append(x)


def RGBtoXYZ(r, g, b):
    rgb = sRGBColor(r / 255, g / 255, b / 255)  # The XYZ color
    xyz = convert_color(rgb, XYZColor)  # Converts the XYZ color to sRGB
    xyzz = xyz.get_value_tuple()  # Converts the color to a tuple
    rgblist = []  # Empty list
    for i in xyzz:  # For loop that converts tuple to floats and appends to a list
        p = float(i)
        if p > 255:
            p = 255
        rgblist.append(p)
    return rgblist


print("White")
print(RGBtoXYZ(255, 255, 255))
print("white-1")
print(RGBtoXYZ(255, 255, 254))
print(RGBtoXYZ(255, 254, 255))
print(RGBtoXYZ(254, 255, 255))
print("")
print("Black")
print(RGBtoXYZ(0, 0, 0))
print("Black-1")
print(RGBtoXYZ(1, 0, 0))
print(RGBtoXYZ(0, 1, 0))
print(RGBtoXYZ(0, 0, 1))
