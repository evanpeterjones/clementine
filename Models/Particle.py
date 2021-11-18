import pygame
import random

from Physics.Visible import Visible
from resources.Utils import random_color

def rand():
    return random.randint(0, 2) - 1

class Particle(Visible):
    def __init__(self, timer: int, color: int = None, width: int = None, x_vel: int = None,
                 y_vel: int = None, *args, **kwargs):

        '''
        shitty/cool thing I just learned about Python.
        If you call a random function in a default parameter, it'll always return the same value
        '''

        if x_vel is None:
            x_vel = rand()
        if y_vel is None:
            y_vel = rand()

        super().__init__(x_vel=x_vel, y_vel=y_vel, *args, **kwargs)

        self.timer = timer
        self.color = color if color is not None else random_color()
        self.width = width if width is not None else random.randint(4, 20)

    def get_velocity(self):
        return [self.x_vel, self.y_vel]

    def update_particle(self):
        super().update()
        self.timer -= 0.1
        self.width = self.width - 1 if self.width > 0 else 0

    def not_exists(self):
        return self.timer <= 0

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.get_position(), self.width)

