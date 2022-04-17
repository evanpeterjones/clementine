import pygame
import sys

from pygame.locals import *

from Physics.Visible import Visible
from System.Dialogue import Dialogue
from System.Clock import Clock
from Models.Player import Player
from Models.Sprite import Sprite
from Models.Map import Map
from resources.Colors import BG

import threading

clock = Clock()
g_vel = 3


# window =

def get_cursor_elements(elements):
    'function to return all of the elements which recieve cursor input'
    return [e for e in elements if e.cursor_control_enabled]

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

            # make cursor invisible
            pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    key_down = False
                    pass
                if event.type == MOUSEMOTION:
                    [i.set_position(pygame.mouse.get_pos()) for i in get_cursor_elements(args[0].elements)]

                # These will always attempt to
                # update the position of whichever item is first in the list
                # So when we switch devices, we should just move them to the first in the list
                # Todo: represent the device list on screen using the elements list and
                #  class reflection to determine what class type each element is
                # Todo: possibly implement a "Playable" interface/class
                if event.type == KEYDOWN:
                    key_down = True
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    else:
                        for i in args[0].elements:
                            i.key(event.key, True)
                if event.type == KEYUP:
                    key_down = False
                    for i in args[0].elements:
                        i.key(event.key, False)

            clock.next_frame_ready()
            pygame.display.update()
            print("cycles available: " + str(clock.AverageCycles))

    return internalLoop


class View:
    def __init__(self, window_size=(1200, 720), c="See ya next time", header="CLEM"):
        pygame.display.set_caption(header)  # set header text

        self.clock = pygame.time.Clock()
        self.WINDOW_SIZE: Tuple[int, int] = window_size  # default will need to be changed through conf file
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)  # initialize the window
        self.close_message: str = c
        self.elements: [Visible] = []

    def add_element(self, new_element: Visible):
        self.elements.append(new_element)

    def exit(self):
        pygame.quit()
        print(self.close_message)
        sys.exit()

    def update_header(self, header):
        """
        :type header: String
        """
        pygame.display.set_caption(header)


class Play(View):
    """
    Present Start Screen and all Animations
    """

    def __init__(self):
        super().__init__(c="peace out", header="Clementine")

        # mouse has to be the first item in the list, always or this breaks
        self.elements.append(Player(x=400, y=200, z=0, x_acc=1, y_acc=1, screen=self.screen,
                                    file_name="Images/character_sswsddddddddxxxxww.png"))
        self.elements.append(Sprite(count=2, screen=self.screen, cursor=True))
        self.elements.append(Sprite(count=2, screen=self.screen, x=200, y=200, x_vel=1))
        self.elements.append(Map(self.screen.get_size()))
        self.particles = []
        # self.music = open("resources/Music/space.mp3")
        self.dialogue = Dialogue()

        # pygame.mixer.music.load(self.music)
        # pygame.mixer.music.play(-1)

        pygame.display.update()

    @GameLoop
    def run(self):
        self.screen.fill(BG)

        # Todo: time element, need a clock in the corner
        # Todo: Todo-list, schedule on the screen :?
        # Todo: Building/House/Apartment map generator
        # Todo: we need to add a Z-index to the elements, and insert into the element list based on that. The only way this would work is if the cursor element is handled differently
        for element in self.elements:
            element.update(all_items=self.elements)

        self.dialogue.update(self.screen)

        return True


class Pause(View):
    def __init__(self):
        super().__init__(c="Yeet", header="Paused")

    @GameLoop
    def run(self):
        return True


class StartScreen(View):
    def __init__(self):
        super().__init__(header="Game Start")
        self.elements.append()

    @GameLoop
    def run(self):

        return True


if __name__ == "__main__":
    pygame.init()  # initialize screen
    GAME = StartScreen() #Play()
    GAME.run()
    print("yo, we outie")
