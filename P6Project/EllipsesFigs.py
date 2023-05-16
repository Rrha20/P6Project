"""
==================
Ellipse with units
==================

Compare the ellipse generated with arcs versus a polygonal approximation.

.. only:: builder_html

   This example requires :download:`basic_units.py <basic_units.py>`
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches


def XYZtoxyY(X, Y, Z):
    a = X / (X + Y + Z)
    b = Y / (X + Y + Z)
    # c = findangle(b, a)
    return a, b


'''

'''

# color1 = [[0.39090996221384566, 0.3044423360552147, 0.7030207255994174], [0.40174042619717043, 0.2960492188505345, 0.7010975880031074], [0.3776573715598278, 0.2629583049529543, 0.6541522933821876], [0.44488243395516947, 0.34374784210818304, 0.6768905586031395], [0.39258631210659173, 0.3031477519160682, 0.7106773153519281], [0.4212774217809241, 0.2896016430114975, 0.6929292645228455], [0.39229915124609993, 0.3174809872094872, 0.6951435118479795], [0.4521814764441494, 0.386511322637109, 0.8070778681792916], [0.35864491883554267, 0.2596903420398085, 0.7212932486145252], [0.40329226271582264, 0.2986021496425355, 0.6952584290377951]]
color1 = [[[0.39412754296211777, 0.3028698921000988, 0.7019514859809306],
           [0.39472936197803293, 0.30257578085699854, 0.7017514945012077]],
          [[0.4040059314005252, 0.29090650422926445, 0.7025263135280517],
           [0.4037800639591041, 0.29141922509688595, 0.702383871754652]],
          [[0.3924774674522168, 0.28752844333590344, 0.6845635500676548],
           [0.39322469167278773, 0.28876726139995845, 0.6860968753402025]],
          [[0.41075952806115423, 0.3104875358419309, 0.6944600445814619],
           [0.4095092935103916, 0.3092689062154808, 0.6951037757595]],
          [[0.39346331996154293, 0.3027753862061111, 0.709414234201485],
           [0.3938699754205794, 0.30260272578139863, 0.708828562314815]],
          [[0.4092167043220926, 0.2954957615266848, 0.6969371816330167],
           [0.40673838626846337, 0.29670692498990997, 0.6977607556339409]],
          [[0.39673718699862853, 0.30740661116283274, 0.6979423290614045],
           [0.3978092766232788, 0.3049729592869348, 0.6986184351279445]],
          [[0.41260500375523035, 0.3208977518656041, 0.7258658248573447],
           [0.41171260761873396, 0.3194182542479547, 0.7240346027000004]],
          [[0.39221947032305676, 0.292416155858104, 0.7040061039199756],
           [0.39373737421942584, 0.29389568836429736, 0.7032245529199954]],
          [[0.4101273853073566, 0.2957000487524789, 0.6854143729582582],
           [0.40934490726878225, 0.2960322783770081, 0.6865413107109581]],
          [[0.40449110537002875, 0.28980515550442787, 0.7028322852085589],
           [0.40335446852106815, 0.2923853300869307, 0.7021154728718237]],
          [[0.4211879907456365, 0.32065237537375096, 0.6890905508613331],
           [0.420084470285144, 0.31957675102332034, 0.6896587406666689]],
          [[0.40994411894198507, 0.29514027123400854, 0.6966954532689118],
           [0.40750356632774787, 0.29633297858329904, 0.6975064773737599]],
          [[0.4216968232335899, 0.335971018891549, 0.7445224960355872],
           [0.4207271226537488, 0.33436335875157935, 0.7425326429701465]],
          [[0.4064188100685574, 0.29727465979379253, 0.690755524069599],
           [0.40499013141191553, 0.2978812574876189, 0.6928131305905177]]]
color1T = [0.4, 0.3, 0.7]
target = XYZtoxyY(0.4, 0.3, 0.7)


def findmid(a1, b1):
    x1 = (a1[0] + b1[0]) / 2
    y1 = (a1[1] + b1[1]) / 2
    z1 = (a1[2] + b1[2]) / 2
    return x1, y1, z1


col1mids = []
for i in range(len(color1)):
    if i % 2 == 0:
        p = findmid(color1[i][0], color1[i][1])
        col1mids.append(p)
Elist = []  # Empty list

for i in col1mids:  # For loop that converts tuple to floats and appends to a list
    print(i)
    smollist = []
    for j in i:
        h = float(j)
        print(type(h))
        smollist.append(h)
    x = smollist
    print(x)
    print('x', type(x), type(x[0]), x[0])
    Elist.append(x)
    smollist = []
print("list", Elist)

print("mids", col1mids)
print(color1)

print('tuple?', Elist[0], type(Elist))
'''
col1XYZ = []
for i in range(len(color1)):
    x1 = Elist[0][i][0]
    y1 = Elist[0][i][1]
    z1 = Elist[0][i][2]
    col1 = XYZtoxyY(x1, y1, z1)
    col1XYZ.append(col1)
'''

col1XYZ = []
for sublist in Elist:
    x1 = sublist[0]
    y1 = sublist[1]
    z1 = sublist[2]
    col1 = XYZtoxyY(x1, y1, z1)
    col1XYZ.append(col1)

col1np = np.array(col1XYZ, dtype=np.float32)
print("col1np", col1np)
print(target)
ellipse_t = cv.fitEllipse(col1np * 2)
(x, y), (minor, major), angles = ellipse_t
print(ellipse_t)
print(x, y, minor, major, angles)

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(211, aspect='auto')
ax.fill(x, y, alpha=0.2, facecolor='yellow',
        edgecolor='yellow', linewidth=1, zorder=1)

e1 = patches.Ellipse((x, y), minor, major, angles)

ax.add_patch(e1)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_box_aspect(1)
'''
ax = fig.add_subplot(212, aspect='equal')
ax.fill(x, y, alpha=0.2, facecolor='green', edgecolor='green', zorder=1)
e2 = patches.Arc((xcenter, ycenter), width, height,
             angle=angle, linewidth=2, fill=False, zorder=2)


ax.add_patch(e2)'''
fig.savefig('arc_compare')

plt.show()

'''
xcenter, ycenter = 0.38*cm, 0.52*cm
width, height = 1e-1*cm, 3e-1*cm
angle = -30

theta = np.deg2rad(np.arange(0.0, 360.0, 1.0))
x = 0.5 * width * np.cos(theta)
y = 0.5 * height * np.sin(theta)

rtheta = np.radians(angle)
R = np.array([
    [np.cos(rtheta), -np.sin(rtheta)],
    [np.sin(rtheta),  np.cos(rtheta)],
    ])


x, y = np.dot(R, [x, y])
x += xcenter
y += ycenter

###############################################################################

fig = plt.figure()
ax = fig.add_subplot(211, aspect='auto')
ax.fill(x, y, alpha=0.2, facecolor='yellow',
        edgecolor='yellow', linewidth=1, zorder=1)

e1 = patches.Ellipse((xcenter, ycenter), width, height,
                     angle=angle, linewidth=2, fill=False, zorder=2)

ax.add_patch(e1)

ax = fig.add_subplot(212, aspect='equal')
ax.fill(x, y, alpha=0.2, facecolor='green', edgecolor='green', zorder=1)
e2 = patches.Ellipse((xcenter, ycenter), width, height,
                     angle=angle, linewidth=2, fill=False, zorder=2)


ax.add_patch(e2)
fig.savefig('ellipse_compare')

###############################################################################

fig = plt.figure()
ax = fig.add_subplot(211, aspect='auto')
ax.fill(x, y, alpha=0.2, facecolor='yellow',
        edgecolor='yellow', linewidth=1, zorder=1)

e1 = patches.Arc((xcenter, ycenter), width, height,
                 angle=angle, linewidth=2, fill=False, zorder=2)

ax.add_patch(e1)

ax = fig.add_subplot(212, aspect='equal')
ax.fill(x, y, alpha=0.2, facecolor='green', edgecolor='green', zorder=1)
e2 = patches.Arc((xcenter, ycenter), width, height,
                 angle=angle, linewidth=2, fill=False, zorder=2)


ax.add_patch(e2)
fig.savefig('arc_compare')

plt.show()
'''
