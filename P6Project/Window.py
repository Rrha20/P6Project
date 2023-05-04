import pygame
from numpy import random
from colormath.color_objects import sRGBColor, XYZColor
from colormath.color_conversions import convert_color

# initialize window
pygame.init()
width = 800
height = 500
win = pygame.display.set_mode([width, height])


# function for drawing the squares
def squarees(col, side):
    color = col
    if side == "left":
        pygame.draw.rect(win, color, pygame.Rect((250, 175), (140, 140)))
    if side == "right":
        pygame.draw.rect(win, color, pygame.Rect((410, 175), (140, 140)))


# function for generating a random color
def randomCol():
    x = random.randint(256)
    y = random.randint(256)
    z = random.randint(256)
    return x, y, z


def XYZtoRGB(x, y, z):
    xyz = XYZColor(x, y, z)  # The XYZ color
    rgb = convert_color(xyz, sRGBColor)  # Converts the XYZ color to sRGB
    rgbb = rgb.get_value_tuple()  # Converts the color to a tuple
    rgblist = []  # Empty list
    for i in rgbb:  # For loop that converts tuple to floats and appends to a list
        x = float(i) * 255
        if x > 255:
            x = 255
        rgblist.append(x)
    return rgblist

def RGBtoXYZ(r, g, b):
    rgb = sRGBColor(r/255, g/255, b/255)  # The XYZ color
    xyz = convert_color(rgb, XYZColor)  # Converts the XYZ color to sRGB
    xyzz = xyz.get_value_tuple()  # Converts the color to a tuple
    rgblist = []  # Empty list
    for i in xyzz:  # For loop that converts tuple to floats and appends to a list
        p = float(i)
        if p > 255:
            p = 255
        rgblist.append(p)
    return rgblist

# font used on buttons
smallfont = pygame.font.SysFont('Corbel', 35)
# rendering a text written in this font
text1 = smallfont.render('Same', True, (255, 255, 255))
text2 = smallfont.render('Diff', True, (255, 255, 255))

print("Red")
print(RGBtoXYZ(255,0,0))
print("Green")
print(RGBtoXYZ(0,255,0))
print("Blue")
print(RGBtoXYZ(0,0,255))
print("Black")
print(RGBtoXYZ(0,0,0))
print("White")
print(RGBtoXYZ(255,255,255))

Directions = [  [0.03797883160764542,   -0.7874845025153955,    -0.6151632032621898],
                [0.6722625212766092,    -0.17205248450998017,   0.7200423911553816],
                [0.1363051541794393,    -0.19763978184289696,   -0.9707519876761579],
                [-0.3771225811044923,   0.9063296619975425,     0.19064391572905182],
                [-0.05610162182861117,  -0.8681803359860506,    -0.4930674520137664],
                [0.17498981461000856,   -0.7077695917901823,    0.6844273297581809],
                [0.15424748415451592,   -0.4810405392959806,    0.8630224291325426],
                [0.13418890295728594,   0.06769853659334661,    -0.9886406053092496],
                [0.643368927393114,     0.029841408658842394,   -0.76497445290303],
                [-0.8168235261819979,   0.27412174611139833,    0.507598852820261]]

# startup stuff
col2 = [0.4, 0.3, 0.7]
Fun1 = [0.8461142062048901, -0.02520778340590566, 0.5324052194654272]
col1 = []
for i in col2:
    x = i + Fun1[0]/5
    col1.append(x)
col1rgb = XYZtoRGB(col1[0], col1[1], col1[2])
col2rgb = XYZtoRGB(col2[0], col2[1], col2[2])
print(col1rgb)
print(col2rgb)
squarees(col1rgb, "right")
LastB = col1
squarees(col2rgb, "left")
LastF = col2
Current = col1
Start = col2
# Many prints for many things
print(LastB)
print(LastF)
print(Current)
print("")
print(Start)
print("")


# function for finding the midpoint between two points
def findMid():
    P1 = LastF
    P2 = LastB
    Perc1 = 0.25
    Perc2 = 0.75
    x = (P1[0] * Perc1 + P2[0] * Perc2)
    y = (P1[1] * Perc1 + P2[1] * Perc2)
    z = (P1[2] * Perc1 + P2[2] * Perc2)
    return [x, y, z]


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width - width / 4 - 140 <= mouse[0] <= width - width / 4 and height / 2 <= mouse[
                1] <= height - height / 4 + 40:
                LastF = Current
                Current = findMid()
                toRGB = XYZtoRGB(Current[0], Current[1], Current[2])
                squarees(toRGB, "right")

                print(LastB)
                print(LastF)
                print(Current)
                print(toRGB)
                print("")
                print(Start)
                print("")

            if width / 4 <= mouse[0] <= width / 4 + 140 and height / 2 <= mouse[1] <= height - height / 4 + 40:
                LastB = Current
                Current = findMid()
                toRGB = XYZtoRGB(Current[0], Current[1], Current[2])
                squarees(toRGB, "right")

                print(LastB)
                print(LastF)
                print(Current)
                print(toRGB)
                print("")
                print(Start)
                print("")

    # fills the screen with a color
    # win.fill((60, 25, 60))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width - width / 4 - 140 <= mouse[0] <= width - width / 4 and height - height / 4 <= mouse[
        1] <= height - height / 4 + 40:
        pygame.draw.rect(win, (170, 170, 170), [width - width / 4 - 140, height - height / 4, 140, 40])

    else:
        pygame.draw.rect(win, (100, 100, 100), [width - width / 4 - 140, height - height / 4, 140, 40])

    # superimposing the text onto our button
    win.blit(text1, [width - width / 4 + 30 - 140, height - height / 4 + 5])

    if width / 4 <= mouse[0] <= width / 4 + 140 and height - height / 4 <= mouse[
        1] <= height - height / 4 + 40:
        pygame.draw.rect(win, (170, 170, 170), [width / 4, height - height / 4, 140, 40])

    else:
        pygame.draw.rect(win, (100, 100, 100), [width / 4, height - height / 4, 140, 40])

    # superimposing the text onto our button
    win.blit(text2, [width / 4 + 30, height - height / 4 + 5])

    # updates the frames of the game
    pygame.display.update()
