import pygame
import random
import sys

from pygame.locals import *

from Models.Particle import Particle
from System.Dialogue import Dialogue
from Models.Player import Player
from Models.Sprite import Sprite
from System.Clock import Clock
from resources.Colors import BG, FG

clock = Clock()
g_vel = 10

#window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def GameLoop(func):
    """
    Decorates game loop functions, to indicate the end of the loop, return false from implementing function
    :type func: Function
    :param func:
    :return: Function
    """

    def internalLoop(*args, **kwargs):
        running = True

        while running:
            # call our game code
            running = func(*args, **kwargs)

            pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    key_down = False
                    pass
                if event.type == MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()

                    [i.set_position(x, y) for i in args[0].elements]

                if event.type == KEYDOWN:
                    key_down = True
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_w:
                        [i.set_y_vel(- (g_vel)) for i in args[0].elements]
                    if event.key == K_a:
                        [i.set_x_vel(- (g_vel)) for i in args[0].elements]
                    if event.key == K_s:
                        [i.set_y_vel(g_vel) for i in args[0].elements]
                    if event.key == K_d:
                        [i.set_x_vel(g_vel) for i in args[0].elements]
                if event.type == KEYUP:
                    if event.key == K_w:
                        [i.set_y_vel(0) for i in args[0].elements]
                    if event.key == K_a:
                        [i.set_x_vel(0) for i in args[0].elements]
                    if event.key == K_s:
                        [i.set_y_vel(0) for i in args[0].elements]
                    if event.key == K_d:
                        [i.set_x_vel(0) for i in args[0].elements]


            #args[0].player.update()
            clock.next_frame_ready()
            pygame.display.update()
            print("cycles available: " + str(clock.AverageCycles))

    return internalLoop


class View:
    def __init__(self, window_size=(1200, 720), c="See ya next time", header="CLEM"):
        pygame.display.set_caption(header)  # set header text

        self.clock = pygame.time.Clock()
        self.WINDOW_SIZE = window_size  # default will need to be changed through conf file
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)  # initialize the window
        self.close_message = c
        self.elements = []
#        self.player = player

    def exit(self):
        pygame.quit()
        print(self.close_message)
        sys.exit()

    def update_header(self, header):
        """
        :type header: String
        """
        pygame.display.set_caption(header)


class StartScreen(View):
    """
    Present Start Screen and all Animations
    """

    def __init__(self):
        super().__init__(c="peace out", header="Start Screen")
        self.elements.append(Player(x=200, y=200, file_name="Images/character_sswsddddddddxxxxww.png", x_acc=1, y_acc=1, screen=self.screen))
        self.elements.append(Sprite(count=2, screen=self.screen))
        self.particles = []
        self.music = open("resources/Music/space.mp3")
        self.dialogue = Dialogue()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)

        pygame.display.update()

    @GameLoop
    def run(self):

        self.screen.fill(BG)

        for element in self.elements:
            element.update()

        self.screen.blit(self.elements[0].get_image(), (200, 200))
        self.dialogue.update(self.screen)

        return True


class Play(View):
    def __init__(self):
        super().__init__(c="Oh my darlin'", header="Game Start")

    @GameLoop
    def run(self):
        return True


if __name__ == "__main__":
    pygame.init()  # initialize screen
    GAME = StartScreen()
    GAME.run()
    print("yo, we outie")
