from colormath import *
from colormath.color_objects import sRGBColor, XYZColor
from colormath.color_conversions import convert_color
from colormath.color_objects import ColorBase, IlluminantMixin
import numpy as np

XYZ = [15.4999257, 20.91432805, 8.15938343]

RGB = []


xyz = XYZColor(0.1, 0.2, 0.3)
rgb = convert_color(xyz, sRGBColor)
rgbb = rgb.get_value_tuple()



print(xyz)
print(rgb)
print(rgbb)