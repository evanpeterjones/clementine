import pygame
import random
import sys
from pygame.locals import *

from Models.Particle import Particle
from Models.Player import Player
from System.Clock import Clock

clock = Clock()


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

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    key_down = False
                    pass
                if event.type == MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    args[0].player.set_position(x, y)
                if event.type == KEYDOWN:
                    key_down = True
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_w:
                        args[0].player.move(0, -1)
                    if event.key == K_a:
                        args[0].player.move(-1, 0)
                    if event.key == K_s:
                        args[0].player.move(0, 1)
                    if event.key == K_d:
                        args[0].player.move(1, 0)

            clock.next_frame_ready()
            pygame.display.update()
            print("cycles available: " + str(clock.AverageCycles))

    return internalLoop


class View:
    def __init__(self, window_size=(900, 500), c="See ya next time", header="CLEM", player=Player()):
        self.clock = pygame.time.Clock()
        self.WINDOW_SIZE = window_size  # default will need to be changed through conf file
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)  # initialize the window
        self.close_message = c
        self.player = player

        pygame.init()  # initialize screen
        pygame.display.set_caption(header)  # set header text

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

        # [location, velocity, timer, color]
        self.particles = []
        self.player = Player(x=200, y=200)
        self.playerImg = pygame.image.load('resources\character.png')

    @staticmethod
    def update_particles(screen, arr_particles):
        for x in arr_particles:
            x.update_particle()
            pygame.draw.circle(screen, x.color, x.get_position(), x.width)
            if x.exists():
                arr_particles.remove(x)

    @GameLoop
    def run(self):

        xpos, ypos = self.player.get_position()

        #self.screen.blit(self.playerImg, (x, y))

        self.screen.fill((0, 0, 0))
        self.particles.append(
            Particle(random.randint(4, 10), x=xpos, y=ypos))
        self.update_particles(self.screen, self.particles)

        return True


class Play(View):
    def __init__(self):
        super().__init__(c="Oh my darlin'", header="Game Start")

    @GameLoop
    def run(self):
        return True


if __name__ == "__main__":
    GAME = StartScreen()
    GAME.run()
    print("yo, we outie")
