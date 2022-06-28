import pygame.locals as pl

from Models.ImageResource import ImageResource
from Physics.Interactive import Interactive


class Player(Interactive, ImageResource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def key(self, key, keydown=False):
        self.set_key_down(key, keydown)

        if key == pl.K_w:
            self.set_y_vel((- self.g_vel) if keydown else 0)
        if key == pl.K_a:
            self.set_x_vel((- self.g_vel) if keydown else 0)
        if key == pl.K_s:
            self.set_y_vel(self.g_vel if keydown else 0)
        if key == pl.K_d:
            self.set_x_vel(self.g_vel if keydown else 0)

    def update(self, all_items=[], **kwargs):
        self.next_frame()
        self.screen.blit(self.get_image(), self.get_position())
        super().update(all_items)

