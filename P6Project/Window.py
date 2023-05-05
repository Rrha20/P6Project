import pygame
from numpy import random
from colormath.color_objects import sRGBColor, XYZColor
from colormath.color_conversions import convert_color
import csv
import time
import datetime

# initialize window
pygame.init()
width = 800
height = 500
win = pygame.display.set_mode([width, height])
curCol = 2

# function for drawing the squares
def squarees(col, side):
    color = col
    if side == "left":
        pygame.draw.rect(win, color, pygame.Rect((250, 175), (140, 140)))
    if side == "right":
        pygame.draw.rect(win, color, pygame.Rect((410, 175), (140, 140)))

def toBlack():
    colorer = (0, 0, 0)
    squarees(colorer, "left")
    squarees(colorer, "right")
    pygame.display.update()

'''
def toString(a, b, c):
    x = str(a)
    y = str(b)
    z = str(c)
    return x, y, z

def randomCol():
    x = random.randint(256)
    y = random.randint(256)
    z = random.randint(256)
    return x, y, z
'''

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

def changeSquare(x):
    f = 0
    if x == 1:
        f = 2
    if x == 2:
        f = 3
    if x == 3:
        f = 1
    return f

def findMid(F, B):
    P1 = F
    print(P1)
    P2 = B
    print(P2)
    Perc1 = 0.25
    Perc2 = 0.75
    a = (P1[0] * Perc1 + P2[0] * Perc2)
    print(P1[0], Perc1, P2[0], Perc2)
    b = (P1[1] * Perc1 + P2[1] * Perc2)
    c = (P1[2] * Perc1 + P2[2] * Perc2)
    print(a, b, c)
    return [a, b, c]



# function for generating a random color
with open('data.csv', mode='a') as data_file:
    # Create a CSV writer object
    data_writer = csv.writer(data_file)

    # Write the header row if the file is empty
    if data_file.tell() == 0:
        data_writer.writerow(['LastB', 'LastF', 'Current'])

    # Add the values of LastB, LastF, and Current to the CSV file




    # font used on buttons
    smallfont = pygame.font.SysFont('Corbel', 35)
    # rendering a text written in this font
    text1 = smallfont.render('Same', True, (255, 255, 255))
    text2 = smallfont.render('Diff', True, (255, 255, 255))

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

    # Color 1
    col1T = [0.4, 0.3, 0.7]
    Fun1 = Directions[7]
    col1P = []
    for i in range(3):
        x = col1T[i] + Fun1[i]/10
        col1P.append(x)
    #print(col1P)
    col1rgbP = XYZtoRGB(col1P[0], col1P[1], col1P[2])
    col1rgbT = XYZtoRGB(col1T[0], col1T[1], col1T[2])
    squarees(col1rgbP, "right")
    LastB1 = col1P
    squarees(col1rgbT, "left")
    LastF1 = col1T
    Current1 = col1P
    Start1 = col1T

    # Color 2
    col2T = [0.6, 0.2, 0.4]
    Fun2 = Directions[4]
    col2P = []
    for i in range(3):
        x = col2T[i] + Fun2[i]/10
        col2P.append(x)
    #print(col2P)
    col2rgbP = XYZtoRGB(col2P[0], col2P[1], col2P[2])
    col2rgbT = XYZtoRGB(col2T[0], col2T[1], col2T[2])
    #squarees(col2rgbP, "right")
    LastB2 = col2P
    #squarees(col2rgbT, "left")
    LastF2 = col2T
    Current2 = col1P
    Start2 = col2T

    # Color 3
    col3T = [0.2, 0.5, 0.1]
    Fun3 = Directions[3]
    col3P = []
    for i in range(3):
        x = col3T[i] + Fun3[i]/10
        col3P.append(x)
    col3rgbP = XYZtoRGB(col3P[0], col3P[1], col3P[2])
    col3rgbT = XYZtoRGB(col3T[0], col3T[1], col3T[2])
    #squarees(col3rgbP, "right")
    LastB3 = col3P
    #squarees(col3rgbT, "left")
    LastF3 = col3T
    Current3 = col3P
    Start3 = col3T


    # function for finding the midpoint between two points
    def Sames(g, current):
        if g == 1:
            Current1 = current
            LastF1 = Current1
            Current1 = findMid(LastF1, LastB1)
            toRGB = XYZtoRGB(Current1[0], Current1[1], Current1[2])
            squarees(toRGB, "right")
            squarees(col1rgbT, "left")
        if g == 2:
            Current2 = current
            LastF2 = Current2
            Current2 = findMid(LastF2, LastB2)
            toRGB = XYZtoRGB(Current2[0], Current2[1], Current2[2])
            squarees(toRGB, "right")
            squarees(col2rgbT, "left")
        if g == 3:
            Current3 = current
            LastF3 = Current3
            Current3 = findMid(LastF3, LastB3)
            toRGB = XYZtoRGB(Current3[0], Current3[1], Current3[2])
            squarees(toRGB, "right")
            squarees(col3rgbT, "left")

    def Diff(g, current):
        if g == 1:
            Current1 = current
            LastB1 = Current1
            Current1 = findMid(LastF1, LastB1)
            toRGB = XYZtoRGB(Current1[0], Current1[1], Current1[2])
            squarees(toRGB, "right")
            squarees(col1rgbT, "left")
        if g == 2:
            Current2 = current
            LastB2 = Current2
            Current2 = findMid(LastF2, LastB2)
            toRGB = XYZtoRGB(Current2[0], Current2[1], Current2[2])
            squarees(toRGB, "right")
            squarees(col2rgbT, "left")
        if g == 3:
            Current3 = current
            LastB3 = Current3
            Current3 = findMid(LastF3, LastB3)
            toRGB = XYZtoRGB(Current3[0], Current3[1], Current3[2])
            squarees(toRGB, "right")
            squarees(col3rgbT, "left")

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
                    # SAME
                    toBlack()
                    time.sleep(1)
                    print(curCol)
                    if curCol == 1:
                        curCol = 2
                        c = Current1
                    elif curCol == 2:
                        curCol = 3
                        c = Current2
                    elif curCol == 3:
                        curCol = 1
                        c = Current3
                    Sames(curCol, c)

                    data_writer.writerow([LastB1, LastF1, Current1])
                    print(curCol)



                if width / 4 <= mouse[0] <= width / 4 + 140 and height / 2 <= mouse[1] <= height - height / 4 + 40:
                    # DIFF
                    toBlack()
                    time.sleep(1)
                    if curCol == 1:
                        curCol = 2
                        c = Current1
                    elif curCol == 2:
                        curCol = 3
                        c = Current2
                    elif curCol == 3:
                        curCol = 1
                        c = Current3
                    Diff(curCol, c)

                    '''
                    print(LastB1)
                    print(LastF1)
                    print(Current1)
                    print(toRGB)
                    print("")
                    print(Start1)
                    print("")
                    '''
                    data_writer.writerow([LastB1, LastF1, Current1])
                    #curCol = changeSquare(curCol)

                    print(curCol)



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
