import pygame

# initialize window

pygame.init()
width = 800
height = 500
win = pygame.display.set_mode([width, height])


def squarees(col, side):
    color = col
    if side == "left":
        pygame.draw.rect(win, color, pygame.Rect((250, 175), (150, 150)))
    if side == "right":
        pygame.draw.rect(win, color, pygame.Rect((400, 175), (150, 150)))


red = (255, 0, 0)
# surf = pygame.surface([width, height])
# draw an elliptical arc
# arc(surface, color, rect, start_angle, stop_angle) -> Rect
# pygame.draw.arc(win, red, (300, 200, 400, 300), 0.5 * PI, 1.5)
# pygame.draw.circle(win, red, (400, 250), 100)
# pygame.draw.rect(win, red, pygame.Rect(30, 30, 60, 60))

squarees((255, 255, 0), "left")
squarees((5, 255, 255), "right")

pygame.display.flip()

# Keeps window open
status = True
while (status):

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
