import csv

import pygame
from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, XYZColor

# initialize window
pygame.init()
width = 800
height = 500
win = pygame.display.set_mode([width, height])
curCol = 1
k = 0.01
Color1 = True
Color2 = True
Color3 = True


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


def finddiff(F, B):
    diff1 = abs(F[0] - B[0])
    diff2 = abs(F[1] - B[1])
    diff3 = abs(F[2] - B[2])
    total = diff3 + diff2 + diff1
    return total


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
    # print(P1)
    P2 = B
    # print(P2)
    Perc1 = 0.25
    Perc2 = 0.75
    a = (P1[0] * Perc1 + P2[0] * Perc2)
    # print(P1[0], Perc1, P2[0], Perc2)
    b = (P1[1] * Perc1 + P2[1] * Perc2)
    c = (P1[2] * Perc1 + P2[2] * Perc2)
    # print(a, b, c)
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

    Directions = [[-0.860898165853627, 0.4207242095148357, 0.2860865036277969],
                  [0.3907130486288363, -0.8869216918721375, 0.24640054001122996],
                  [-0.3544532794614195, -0.5876457338666639, -0.7273481725744246],
                  [0.6718842280712661, 0.6548995349494559, -0.3459453471172367],
                  [-0.5543168124612634, 0.2353554443646269, 0.7983361987475661],
                  [0.860898165853627, -0.4207242095148357, -0.2860865036277969],
                  [-0.3907130486288363, 0.8869216918721375, -0.24640054001122996],
                  [0.3544532794614195, 0.5876457338666639, 0.7273481725744246],
                  [-0.6718842280712661, -0.6548995349494559, 0.3459453471172367],
                  [0.5543168124612634, -0.2353554443646269, -0.7983361987475661],
                  ]

    # Color 1
    col1T = [0.4, 0.3, 0.7]
    Fun1 = Directions[1]
    col1P = []
    for i in range(3):
        x = col1T[i] + Fun1[i] / 5
        col1P.append(x)
    # print(col1P)
    print("color 1")
    col1rgbP = XYZtoRGB(col1P[0], col1P[1], col1P[2])
    col1rgbT = XYZtoRGB(col1T[0], col1T[1], col1T[2])
    print(col1T)
    print(col1P)
    print(col1rgbT)
    print(col1rgbP)
    squarees(col1rgbP, "right")
    LastB1 = col1P
    squarees(col1rgbT, "left")
    LastF1 = col1T
    Current1 = col1P
    Start1 = col1T

    # Color 2
    col2T = [0.2, 0.2, 0.5]
    Fun2 = Directions[1]
    col2P = []
    for i in range(3):
        x = col2T[i] + Fun2[i] / 5
        col2P.append(x)
    col2rgbP = XYZtoRGB(col2P[0], col2P[1], col2P[2])
    col2rgbT = XYZtoRGB(col2T[0], col2T[1], col2T[2])
    print("color2")
    print(col2T)
    print(col2P)
    print(col2rgbT)
    print(col2rgbP)
    # squarees(col2rgbP, "right")
    LastB2 = col2P
    # squarees(col2rgbT, "left")
    LastF2 = col2T
    Current2 = col2P
    Start2 = col2T

    # Color 3
    col3T = [0.2, 0.4, 0.1]
    Fun3 = Directions[1]
    col3P = []
    for i in range(3):
        x = col3T[i] + Fun3[i] / 5
        col3P.append(x)
    col3rgbP = XYZtoRGB(col3P[0], col3P[1], col3P[2])
    col3rgbT = XYZtoRGB(col3T[0], col3T[1], col3T[2])
    print("color3")
    print(col3T)
    print(col3P)
    print(col3rgbT)
    print(col3rgbP)
    # squarees(col3rgbP, "right")
    LastB3 = col3P
    # squarees(col3rgbT, "left")
    LastF3 = col3T
    Current3 = col3P
    Start3 = col3T


    # function for finding the midpoint between two points
    def Sames(g, current):
        LF = 0
        Cur = 0
        if g == 1:
            Current1 = current
            LastF1 = Current1
            Current1 = findMid(LastF1, LastB1)
            LF = LastF1
            Cur = Current1
        if g == 2:
            Current2 = current
            LastF2 = Current2
            Current2 = findMid(LastF2, LastB2)
            LF = LastF2
            Cur = Current2
        if g == 3:
            Current3 = current
            LastF3 = Current3
            Current3 = findMid(LastF3, LastB3)
            LF = LastF3
            Cur = Current3
        returnerer = [LF, Cur]
        print(returnerer)
        return returnerer


    def Diff(g, current):
        LB = 0
        Cur = 0
        if g == 1:
            Current1 = current
            LastB1 = Current1
            Current1 = findMid(LastF1, LastB1)

            LB = LastB1
            Cur = Current1
        if g == 2:
            Current2 = current
            # print(Current2)
            LastB2 = Current2
            Current2 = findMid(LastF2, LastB2)
            # print(Current2)

            LB = LastB2
            Cur = Current2
        if g == 3:
            Current3 = current
            LastB3 = Current3
            Current3 = findMid(LastF3, LastB3)
            LB = LastB3
            Cur = Current3
        returnerer = [LB, Cur]
        return returnerer


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
                    # time.sleep(1)
                    # print(curCol)
                    if curCol == 1:
                        if Color1:
                            c = Current1
                            take = Sames(curCol, c)
                            LastF1 = take[0]
                            Current1 = take[1]
                            t = finddiff(LastF1, LastB1)
                            print(t)
                            if t < k:
                                if Color1:
                                    data_writer.writerow(['Color1'])
                                    Color1 = False
                                    data_writer.writerow([LastB1, LastF1, Current1])
                        curCol = 2
                        print(Current2)
                        toRGB2 = XYZtoRGB(Current2[0], Current2[1], Current2[2])
                        squarees(toRGB2, "right")
                        squarees(col2rgbT, "left")
                    elif curCol == 2:
                        if Color2:
                            c = Current2
                            take = Sames(curCol, c)
                            LastF2 = take[0]
                            Current2 = take[1]
                            t = finddiff(LastF2, LastB2)
                            print(t)
                            '''
                            print(LastF2)
                            print(LastB2)
                            print(Current2)
                            print(t)'''
                            if t < k:
                                if Color2:
                                    data_writer.writerow(['Color2'])
                                    Color2 = False
                                    data_writer.writerow([LastB2, LastF2, Current2])
                        curCol = 3
                        print(Current3)
                        toRGB3 = XYZtoRGB(Current3[0], Current3[1], Current3[2])
                        squarees(toRGB3, "right")
                        squarees(col3rgbT, "left")
                    elif curCol == 3:
                        if Color3:
                            c = Current3
                            take = Sames(curCol, c)
                            LastF3 = take[0]
                            Current3 = take[1]
                            t = finddiff(LastF3, LastB3)
                            print(t)
                            if t < k:
                                if Color3:
                                    data_writer.writerow(['Color3'])
                                    Color3 = False
                                    data_writer.writerow([LastB3, LastF3, Current3])

                        curCol = 1
                        print(Current1)
                        toRGB1 = XYZtoRGB(Current1[0], Current1[1], Current1[2])
                        squarees(toRGB1, "right")
                        squarees(col1rgbT, "left")
                    print(curCol)

                if width / 4 <= mouse[0] <= width / 4 + 140 and height / 2 <= mouse[1] <= height - height / 4 + 40:
                    # DIFF
                    toBlack()
                    # time.sleep(1)
                    if curCol == 1:
                        if Color1:
                            c = Current1
                            take = Diff(curCol, c)
                            LastB1 = take[0]
                            Current1 = take[1]
                            t = finddiff(LastF1, LastB1)
                            if t < k:
                                if Color1:
                                    data_writer.writerow(['Color1'])
                                    Color1 = False
                                    data_writer.writerow([LastB1, LastF1, Current1])
                        curCol = 2
                        print(Current2)
                        toRGB2 = XYZtoRGB(Current2[0], Current2[1], Current2[2])
                        squarees(toRGB2, "right")
                        squarees(col2rgbT, "left")

                    elif curCol == 2:
                        if Color2:
                            c = Current2
                            take = Diff(curCol, c)
                            LastB2 = take[0]
                            Current2 = take[1]
                            t = finddiff(LastF2, LastB2)
                            '''
                            print(LastF2)
                            print(LastB2)
                            print(Current2)
                            print(t)'''
                            if t < k:
                                if Color2:
                                    data_writer.writerow(['Color2'])
                                    Color2 = False
                                    data_writer.writerow([LastB2, LastF2, Current2])
                        curCol = 3
                        print(Current3)
                        toRGB3 = XYZtoRGB(Current3[0], Current3[1], Current3[2])
                        squarees(toRGB3, "right")
                        squarees(col3rgbT, "left")
                    elif curCol == 3:
                        if Color3:
                            c = Current3
                            take = Diff(curCol, c)
                            LastB3 = take[0]
                            Current3 = take[1]
                            t = finddiff(LastF3, LastB3)
                            if t < k:
                                if Color3:
                                    data_writer.writerow(['Color3'])
                                    Color3 = False
                                    data_writer.writerow([LastB3, LastF3, Current3])

                        curCol = 1
                        print(Current1)
                        toRGB1 = XYZtoRGB(Current1[0], Current1[1], Current1[2])
                        squarees(toRGB1, "right")
                        squarees(col1rgbT, "left")

                    '''
                    print(LastB1)
                    print(LastF1)
                    print(Current1)
                    print(toRGB)
                    print("")
                    print(Start1)
                    print("")
                    '''
                    # data_writer.writerow([LastB1, LastF1, Current1])
                    # curCol = changeSquare(curCol)

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
