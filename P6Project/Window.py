import pygame
from numpy import *
import colour as c


XYZS = [0.2, 0.3, 0.5]
XYZT = [0.5, 0.1, 0.7]

RGBS = c.XYZ_to_RGB(XYZS)
RGBT = c.XYZ_to_RGB(XYZT)


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


# font used on buttons
smallfont = pygame.font.SysFont('Corbel', 35)
# rendering a text written in this font
text1 = smallfont.render('Same', True, (255, 255, 255))
text2 = smallfont.render('Diff', True, (255, 255, 255))

# startup stuff
col1 = randomCol()
col2 = randomCol()
squarees(RGBT, "right")
LastB = RGBT
squarees(RGBS, "left")
LastF = RGBS
Current = RGBT
Start = RGBS
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
    x = (P1[0] + P2[0]) / 2
    y = (P1[1] + P2[1]) / 2
    z = (P1[2] + P2[2]) / 2
    Current = [x, y, z]
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
                squarees(Current, "right")

                print(LastB)
                print(LastF)
                print(Current)
                print("")
                print(Start)
                print("")

            if width / 4 <= mouse[0] <= width / 4 + 140 and height / 2 <= mouse[1] <= height - height / 4 + 40:
                LastB = Current
                Current = findMid()
                squarees(Current, "right")
                print(LastB)
                print(LastF)
                print(Current)
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
