import pygame
import random

from Models.Particle import Particle
from Physics.Visible import Visible


class Sprite(Visible):
    def __init__(self, generator=Particle, *args, **kwargs):
        self.__type = generator
        self.__particles = []
        super().__init__(*args, **kwargs)

    def update_generators(self):
        for x in self.__particles:
            x.update_particle()
            pygame.draw.circle(self.screen, x.color, x.get_position(), x.width)
            if x.exists():
                self.__particles.remove(x)

    def update(self):
        self.__particles.append(self.__type(random.randint(4, 10), x=self.x_pos, y=self.y_pos))
        self.update_generators()
        super().update()
