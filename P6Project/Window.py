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
    return ((x, y, z))

def XYZtoRGB(x, y, z):
    xyz = XYZColor(x, y, z)                 # The XYZ color
    rgb = convert_color(xyz, sRGBColor)     # Converts the XYZ color to sRGB
    rgbb = rgb.get_value_tuple()            # Converts the color to a tuple
    rgblist = []                            # Empty list
    for i in rgbb:                          # For loop that converts tuple to floats and appends to a list
        x = float(i) * 255
        if x > 255:
            x = 255
        rgblist.append(x)
    return rgblist

# font used on buttons
smallfont = pygame.font.SysFont('Corbel', 35)
# rendering a text written in this font
text1 = smallfont.render('Same', True, (255, 255, 255))
text2 = smallfont.render('Diff', True, (255, 255, 255))

# startup stuff
col1 = [0.2, 0.45, 0.1]
col1rgb = XYZtoRGB(col1[0], col1[1], col1[2])
print(col1rgb)
col2 = [0.455, 0.25, 0.3]
col2rgb = XYZtoRGB(col2[0], col2[1], col2[2])
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
    x = (P1[0]*Perc1 + P2[0]*Perc2)
    y = (P1[1]*Perc1+ P2[1]*Perc2)
    z = (P1[2]*Perc1 + P2[2]*Perc2)
    return [x, y, z]


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width - width / 4 - 140  <= mouse[0] <= width - width / 4 and height / 2 <= mouse[1] <= height - height / 4 + 40:
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
