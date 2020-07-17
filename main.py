import pygame
import random
import sys

from pygame.locals import *

from Models.Particle import Particle
from Models.Player import Player
from System.Clock import Clock
from resources.Colors import BG, FG

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
                    args[0].player.set_position(x, y)
                if event.type == KEYDOWN:
                    key_down = True
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_w:
                        args[0].player.set_y_vel(-5)
                    if event.key == K_a:
                        args[0].player.set_x_vel(-5)
                    if event.key == K_s:
                        args[0].player.set_y_vel(5)
                    if event.key == K_d:
                        args[0].player.set_x_vel(5)
                if event.type == KEYUP:
                    if event.key == K_w:
                        args[0].player.set_y_vel(0)
                    if event.key == K_a:
                        args[0].player.set_x_vel(0)
                    if event.key == K_s:
                        args[0].player.set_y_vel(0)
                    if event.key == K_d:
                        args[0].player.set_x_vel(0)


            args[0].player.update()
            clock.next_frame_ready()
            pygame.display.update()
            print("cycles available: " + str(clock.AverageCycles))

    return internalLoop


class View:
    def __init__(self, window_size=(1200, 720), c="See ya next time", header="CLEM", player=None):
        pygame.display.set_caption(header)  # set header text

        self.clock = pygame.time.Clock()
        self.WINDOW_SIZE = window_size  # default will need to be changed through conf file
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)  # initialize the window
        self.close_message = c
        self.player = player

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

        self.particles = []
#        self.player = Player(x=200, y=200, file_name="coffeepot_static_1.png", x_acc=1, y_acc=1)
        self.player = Player(x=200, y=200, file_name="steve_standing_1.png", x_acc=1, y_acc=1)
        #self.player = Player(x=200, y=200, file_name='steve_standing_1.png')


    @staticmethod
    def update_particles(screen, arr_particles):
        for x in arr_particles:
            x.update_particle()
            pygame.draw.circle(screen, x.color, x.get_position(), x.width)
            if x.exists():
                arr_particles.remove(x)

                # below might be better?
                '''for i, p in sorted(enumerate(arr_particles), reverse=True):
            p.update_particle()
            pygame.draw.circle(screen, p.color, p.get_position(), p.width)
            if p.exists():
                arr_particles.pop(i)
'''

    @GameLoop
    def run(self):

        self.screen.fill(BG)

        xpos, ypos = self.player.get_position()

        self.particles.append(Particle(random.randint(4, 10), x=xpos, y=ypos))
        self.update_particles(self.screen, self.particles)

        self.particles.append(
            Particle(random.randint(4, 10), x=xpos, y=ypos))

        self.update_particles(self.screen, self.particles)
        self.player.get_position()
        self.screen.blit(self.player.get_image(), (xpos, ypos))

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
