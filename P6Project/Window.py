import csv
import time

import numpy as np
import pygame
from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, XYZColor

# initialize window
pygame.init()
width = 800
height = 600
# Scales the window to full screen in 4:3 scale
win = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
# Fill the background color
black = (0, 0, 0)
grey = (150, 150, 150)
BGColor = grey
win.fill(BGColor)
curCol = 1  # Counter for which color is being shown
k = 0.005  # Max difference between LastF and LastB before it finishes
# Checks if the color is still unfinished
Color1 = True
Color2 = True
Color3 = True


# function for drawing the squares
def squarees(col, side):
    color = col
    if side == "left":
        pygame.draw.rect(win, color, pygame.Rect((width / 2 - 150, height / 2 - 75), (140, 140)))
    if side == "right":
        pygame.draw.rect(win, color, pygame.Rect((width / 2 + 10, height / 2 - 75), (140, 140)))


# Covers the squares with the background color during the delay
def toBlack():
    colorer = BGColor
    squarees(colorer, "left")
    squarees(colorer, "right")
    pygame.display.update()


# Converts XYZ color to RGB
def XYZtoRGB(x, y, z):
    xyz = XYZColor(x, y, z)  # The XYZ color
    rgb = convert_color(xyz, sRGBColor)  # Converts the XYZ color to sRGB
    rgbb = rgb.get_value_tuple()  # Converts the color to a tuple
    rgblist = []  # Empty list
    for i in rgbb:  # For loop that converts tuple to floats and appends to a list
        x = float(i) * 255  # Converts to a float and RGB value
        if x > 255:
            x = 255
        rgblist.append(x)
    return rgblist


'''
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
'''


# Finds the difference between LastF and LastB
def finddiff(F, B):
    diff1 = abs(F[0] - B[0])
    diff2 = abs(F[1] - B[1])
    diff3 = abs(F[2] - B[2])
    total = diff3 + diff2 + diff1
    return total


# Changes the curcol value to indicate which square is displayed next
def changeSquare(x):
    f = 0
    if x == 1:
        f = 2
    if x == 2:
        f = 3
    if x == 3:
        f = 1
    return f


# Finds a midpoint between LastF and LastB
def findMid(F, B):
    P1 = F
    # print(P1)
    P2 = B
    # print(P2)
    r = np.random.uniform(0.05, 0.5)  # Randomizes a value
    # LastB always have a higher ratio unless the random number is 0.5
    Perc1 = r  # Perc1 is always multiplied to LastF
    Perc2 = 1 - r  # Perc2 is always multiplied to LastF
    a = (P1[0] * Perc1 + P2[0] * Perc2)
    b = (P1[1] * Perc1 + P2[1] * Perc2)
    c = (P1[2] * Perc1 + P2[2] * Perc2)
    return [a, b, c]  # Returns a list of new XYZ values


# Opens a CSV file to write data into
with open('data.csv', mode='a') as data_file:
    # Create a CSV writer object
    data_writer = csv.writer(data_file)

    # Write the header row if the file is empty
    if data_file.tell() == 0:
        data_writer.writerow(['LastB', 'LastF'])
    data_writer.writerow(['Function 10'])

    # font used on buttons
    smallfont = pygame.font.SysFont('Corbel', 35)
    # rendering a text written in this font
    text1 = smallfont.render('Same', True, (255, 255, 255))
    text2 = smallfont.render('Different', True, (255, 255, 255))

    # Direction vectors used.
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
    # Changes the direction vector used for all colors
    Fun = Directions[9]

    # Color 1
    col1T = [0.4, 0.3, 0.7]  # Target color
    col1P = []  # Start point color
    # For loop calculates the start point color based on the direction vector
    for i in range(3):
        x = col1T[i] + Fun[i] / 5
        col1P.append(x)
    # Converts colors to RGB for display
    col1rgbP = XYZtoRGB(col1P[0], col1P[1], col1P[2])
    col1rgbT = XYZtoRGB(col1T[0], col1T[1], col1T[2])
    # Draws the squares of color 1
    squarees(col1rgbP, "right")
    squarees(col1rgbT, "left")
    # Initilizes the LastB, LastF and Current variables
    LastB1 = col1P
    LastF1 = col1T
    Current1 = col1P
    Start1 = col1T

    # Color 2
    col2T = [0.2, 0.2, 0.5]
    col2P = []
    for i in range(3):
        x = col2T[i] + Fun[i] / 5
        col2P.append(x)
    col2rgbP = XYZtoRGB(col2P[0], col2P[1], col2P[2])
    col2rgbT = XYZtoRGB(col2T[0], col2T[1], col2T[2])
    LastB2 = col2P
    LastF2 = col2T
    Current2 = col2P
    Start2 = col2T

    # Color 3
    col3T = [0.2, 0.4, 0.1]
    col3P = []
    for i in range(3):
        x = col3T[i] + Fun[i] / 5
        col3P.append(x)
    col3rgbP = XYZtoRGB(col3P[0], col3P[1], col3P[2])
    col3rgbT = XYZtoRGB(col3T[0], col3T[1], col3T[2])
    LastB3 = col3P
    LastF3 = col3T
    Current3 = col3P
    Start3 = col3T


    # Function for changing the values of the variables for the color based on the curcol value when click "Same"
    def Sames(g, current):
        LF = 0
        Cur = 0
        if g == 1:
            Current1 = current
            LastF1 = Current1  # Sets LastF to old Current value
            Current1 = findMid(LastF1, LastB1)  # Calculates the new Current value
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
        # Returns the new LastF and Current value
        returnerer = [LF, Cur]
        return returnerer


    # Function for changing the values of the variables for the color based on the curcol value when click "Different"
    def Diff(g, current):
        LB = 0
        Cur = 0
        if g == 1:
            Current1 = current
            LastB1 = Current1  # Sets LastF to old Current value
            Current1 = findMid(LastF1, LastB1)  # Calculates the new Current value
            LB = LastB1
            Cur = Current1
        if g == 2:
            Current2 = current
            LastB2 = Current2
            Current2 = findMid(LastF2, LastB2)
            LB = LastB2
            Cur = Current2
        if g == 3:
            Current3 = current
            LastB3 = Current3
            Current3 = findMid(LastF3, LastB3)
            LB = LastB3
            Cur = Current3
        # Returns the new LastF and Current value
        returnerer = [LB, Cur]
        return returnerer


    # Keeps pygame window open until its being quit
    while True:
        # Keeps track of events
        for ev in pygame.event.get():

            # If the X or any key is pressed, the window closes
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.KEYDOWN:
                pygame.quit()

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the functions run
                if width / 2 + 10 <= mouse[0] <= width / 2 + 150 and height / 2 <= mouse[
                    1] <= height - height / 4 + 40:
                    # SAME
                    # Covers the squares with background color and delays for 1.5 seconds
                    toBlack()
                    time.sleep(1.5)

                    # Does calculations for the current color (curcol) and displays the next color
                    if curCol == 1:
                        if Color1:
                            c = Current1
                            take = Sames(curCol, c)  # Calculates new LastF and Current values
                            LastF1 = take[0]
                            Current1 = take[1]
                            # Finds the difference between LastF and LastB. If the value is lower than k
                            # the color is finished and LastF and LastB is input into the CSV document
                            t = finddiff(LastF1, LastB1)
                            if t < k:
                                if Color1:
                                    data_writer.writerow(['Color1'])
                                    Color1 = False
                                    data_writer.writerow([LastB1, LastF1])
                        # Changes curCol to next color value and displays the next colors
                        curCol = 2
                        toRGB2 = XYZtoRGB(Current2[0], Current2[1], Current2[2])
                        # Randomizes which side each color goes on
                        i = np.random.randint(1, 3)
                        if i == 1:
                            squarees(toRGB2, "right")
                            squarees(col2rgbT, "left")
                        elif i == 2:
                            squarees(toRGB2, "left")
                            squarees(col2rgbT, "right")
                    elif curCol == 2:
                        if Color2:
                            c = Current2
                            take = Sames(curCol, c)
                            LastF2 = take[0]
                            Current2 = take[1]
                            t = finddiff(LastF2, LastB2)
                            if t < k:
                                if Color2:
                                    data_writer.writerow(['Color2'])
                                    Color2 = False
                                    data_writer.writerow([LastB2, LastF2])
                        curCol = 3
                        toRGB3 = XYZtoRGB(Current3[0], Current3[1], Current3[2])
                        i = np.random.randint(1, 3)
                        if i == 1:
                            squarees(toRGB3, "right")
                            squarees(col3rgbT, "left")
                        elif i == 2:
                            squarees(toRGB3, "left")
                            squarees(col3rgbT, "right")

                    elif curCol == 3:
                        if Color3:
                            c = Current3
                            take = Sames(curCol, c)
                            LastF3 = take[0]
                            Current3 = take[1]
                            t = finddiff(LastF3, LastB3)
                            if t < k:
                                if Color3:
                                    data_writer.writerow(['Color3'])
                                    Color3 = False
                                    data_writer.writerow([LastB3, LastF3])

                        curCol = 1
                        toRGB1 = XYZtoRGB(Current1[0], Current1[1], Current1[2])
                        i = np.random.randint(1, 3)
                        if i == 1:
                            squarees(toRGB1, "right")
                            squarees(col1rgbT, "left")
                        elif i == 2:
                            squarees(toRGB1, "left")
                            squarees(col1rgbT, "right")

                    # Checks if all colors are finished, and if so the window closes
                    if not Color1:
                        if not Color2:
                            if not Color3:
                                pygame.quit()

                if width / 2 - 150 <= mouse[0] <= width / 2 - 150 + 140 and height / 2 <= mouse[
                    1] <= height - height / 4 + 40:
                    # DIFF
                    # Covers the squares with background color and delays for 1.5 seconds
                    toBlack()
                    time.sleep(1.5)

                    # Does calculations for the current color (curcol) and displays the next color
                    if curCol == 1:
                        if Color1:
                            c = Current1
                            take = Diff(curCol, c)  # Calculates new LastB and Current values
                            LastB1 = take[0]
                            Current1 = take[1]
                            # Finds the difference between LastF and LastB. If the value is lower than k
                            # the color is finished and LastF and LastB is input into the CSV document
                            t = finddiff(LastF1, LastB1)
                            if t < k:
                                if Color1:
                                    data_writer.writerow(['Color1'])
                                    Color1 = False
                                    data_writer.writerow([LastB1, LastF1])
                        # Changes curCol to next color value and displays the next colors
                        curCol = 2
                        toRGB2 = XYZtoRGB(Current2[0], Current2[1], Current2[2])
                        # Randomizes which side each color goes on
                        i = np.random.randint(1, 3)
                        if i == 1:
                            squarees(toRGB2, "right")
                            squarees(col2rgbT, "left")
                        elif i == 2:
                            squarees(toRGB2, "left")
                            squarees(col2rgbT, "right")
                    elif curCol == 2:
                        if Color2:
                            c = Current2
                            take = Diff(curCol, c)
                            LastB2 = take[0]
                            Current2 = take[1]
                            t = finddiff(LastF2, LastB2)
                            if t < k:
                                if Color2:
                                    data_writer.writerow(['Color2'])
                                    Color2 = False
                                    data_writer.writerow([LastB2, LastF2])
                        curCol = 3
                        toRGB3 = XYZtoRGB(Current3[0], Current3[1], Current3[2])
                        i = np.random.randint(1, 3)
                        if i == 1:
                            squarees(toRGB3, "right")
                            squarees(col3rgbT, "left")
                        elif i == 2:
                            squarees(toRGB3, "left")
                            squarees(col3rgbT, "right")
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
                                    data_writer.writerow([LastB3, LastF3])
                        curCol = 1
                        toRGB1 = XYZtoRGB(Current1[0], Current1[1], Current1[2])
                        i = np.random.randint(1, 3)
                        if i == 1:
                            squarees(toRGB1, "right")
                            squarees(col1rgbT, "left")
                        elif i == 2:
                            squarees(toRGB1, "left")
                            squarees(col1rgbT, "right")
                    # Checks if all colors are finished, and if so the window closes
                    if not Color1:
                        if not Color2:
                            if not Color3:
                                pygame.quit()

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 2 + 10 <= mouse[0] <= width / 2 + 150 and height - height / 4 <= mouse[
            1] <= height - height / 4 + 40:
            pygame.draw.rect(win, (170, 170, 170), [width / 2 + 10, height - height / 4, 140, 40])

        else:
            pygame.draw.rect(win, (100, 100, 100), [width / 2 + 10, height - height / 4, 140, 40])
        # superimposing the text onto our button
        win.blit(text1, [width / 2 + 10 + 30, height - height / 4 + 5])

        if width / 2 - 150 <= mouse[0] <= width / 2 - 150 + 140 and height - height / 4 <= mouse[
            1] <= height - height / 4 + 40:
            pygame.draw.rect(win, (170, 170, 170), [width / 2 - 150, height - height / 4, 140, 40])

        else:
            pygame.draw.rect(win, (100, 100, 100), [width / 2 - 150, height - height / 4, 140, 40])

        # superimposing the text onto our button
        win.blit(text2, [width / 2 - 150 + 5, height - height / 4 + 5])

        # updates the frames of the game
        pygame.display.update()
