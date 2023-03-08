import os
from typing import Tuple

import pygame
import sys

from pygame.locals import *

from Physics.Visible import Visible
from System.Text import Text
from System.Clock import Clock
from Models.Player import Player
from Models.Sprite import Sprite
from Models.Map import Map
from resources.Colors import BG

# import threading

clock = Clock()
g_vel = 3


# window =

def get_cursor_elements(elements):
    'function to return all of the elements which recieve cursor input'
    return [e for e in elements if e.cursor_control_enabled]


class EscapePressed(Exception):
    def __init__(self):
        pass


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
                if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                    [i.key(event.type) for i in get_cursor_elements(args[0].elements)]

                # These will always attempt to
                # update the position of whichever item is first in the list
                # So when we switch devices, we should just move them to the first in the list
                # Todo: represent the device list on screen using the elements list and
                #  class reflection to determine what class type each element is
                # Todo: possibly implement a "Playable" interface/class
                if event.type == KEYDOWN:
                    key_down = True
                    if event.key == K_ESCAPE:
                        raise EscapePressed
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


def safe_get_window():
    try:
        return pygame.display.get_surface().get_size()
    except AttributeError:
        return None


class View:
    def __init__(self,
                 window_size=(1200, 720),
                 img=os.path.join('resources', 'Images', 'coffeepot_x.png'),
                 header="Clementine"):
        pygame.display.set_caption(header)  # set header text
        pygame_icon = pygame.image.load(img)
        pygame.display.set_icon(pygame_icon)
        self.clock = pygame.time.Clock()
        window = safe_get_window()
        self.screen = pygame.display.set_mode((window if window else window_size), pygame.RESIZABLE)

        self.elements: [Visible] = []

    def element(self, new_element: Visible):
        self.elements.append(new_element)

    def update_header(self, header):
        pygame.display.set_caption(header)

    @GameLoop
    def run(self):
        self.screen.fill(BG)

        # Todo: time element, need a clock in the corner
        #  Todo: Todo-list, schedule on the screen :?
        #  Todo: Building/House/Apartment map generator
        #   Todo: we need to add a Z-index to the elements, and insert into the
        #   element list based on that. The only way this would work is if the cursor element is handled differently
        for element in self.elements:
            element.update(all_items=self.elements)
            element.draw(self.screen)

        return True


class Play(View):
    """
    Present Start Screen and all Animations
    """

    def __init__(self):
        super().__init__(header="Cabin in the Woods")

        self.element(Player(x=400, y=200, z=0, x_acc=1, y_acc=1,
                            file_name="Images/character_sswsddddddddxxxxww.png"))
        self.element(Sprite(count=2, width=5, height=5, cursor=True))
        self.element(Sprite(count=2, x=200, y=200, x_acc=2))
        self.element(Sprite(count=2, x=400, y=400, y_acc=20))
        self.element(Map(self.screen.get_size()))


class Pause(View):
    def __init__(self):
        super().__init__(header="Paused")
        self.element(Sprite(count=2, cursor=True))
        self.element(Text(text="Start", y=60))
        self.element(Text(text="Exit", y=100))

class StartScreen(View):
    def __init__(self):
        super().__init__(header="Game Start")
        self.element(Text(text="Start", y=60))
        self.element(Text(text="Exit", y=100))


if __name__ == "__main__":
    pygame.init()
    Continue = True

    Window: [View] = [Play()]

    while Continue:
        try:
            Window[-1].run()
        except EscapePressed:
            if isinstance(Window[-1], Play):
                Window.append(Pause())
            else:
                Window.pop()
