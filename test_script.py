# SETUP IMPORTS ---------------------------------------------#
import pygame,sys,random

# SETUP WINDOW ----------------------------------------------#
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game test env')
screen=pygame.display.set_mode((500, 500),0,32)


# GAME LOOP -------------------------------------------------#
while True:

    # CODE HERE:

    # handle exiting ----------------------------------------#
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # update ------------------------------------------------#
    pygame.display.update()




