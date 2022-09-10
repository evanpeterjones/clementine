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

    def contains(self, x, y):
        # Todo: rewrite this using sin function, this pretends we're a square
        return ((self.x_pos - (self.width / 2)) <= x <= (self.x_pos + (self.width / 2)) and
                (self.y_pos - (self.height / 2)) <= y <= (self.y_pos + (self.height / 2)))

    def key(self, key, keydown=False):
        pass
    
    def update_generators(self):
        for x in self.__particles:
            x.update_particle()

            if x.not_exists():
                self.__particles.remove(x)

    def update(self, vel: tuple = (4, 10), all_items=[]):
        # Todo: implement a follow function so this can trail around the player
        for i in range(self.__count):
            self.__particles.append(self.__type(random.randint(vel[0], vel[1]), x=self.x_pos, y=self.y_pos))
        self.update_generators()
        super().update(all_items=all_items)

    def draw(self, screen):
        for x in self.__particles:
            x.draw(screen)