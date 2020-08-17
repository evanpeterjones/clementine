import pygame
import random

from Models.Particle import Particle
from Physics.Visible import Visible

'''
Class to Generate and process a bunch of particles
'''


class Sprite(Visible):
    def __init__(self, generator: Visible = Particle, count: int = 1, *args, **kwargs):
        self.__type = generator
        self.__count = count
        self.__particles = []
        super().__init__(*args, **kwargs)

    def update_generators(self):
        for x in self.__particles:
            x.update_particle()
            x.draw()

            if x.not_exists():
                self.__particles.remove(x)

    def update(self, vel: tuple = (4, 10)):
        for i in range(self.__count):
            self.__particles.append(self.__type(random.randint(vel[0], vel[1]), x=self.x_pos, y=self.y_pos, screen=self.screen))
        self.update_generators()
        super().update()
