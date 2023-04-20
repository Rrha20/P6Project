from colormath.color_objects import sRGBColor, XYZColor
from colormath.color_conversions import convert_color


xyz = XYZColor(0.4, 0.2, 0.3)           # The XYZ color
rgb = convert_color(xyz, sRGBColor)     # Converts the XYZ color to sRGB
rgbb = rgb.get_value_tuple()            # Converts the color to a tuple
rgblist = []                            # Empty list
for i in rgbb:                          # For loop that converts tuple to floats and appends to a list
    x = float(i) *255
    rgblist.append(x)
    print(rgblist)

print(xyz)
print(rgb)
print(rgbb)