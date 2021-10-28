import pygame.locals as pl

from Models.ImageResource import ImageResource
from Physics.Interactive import Interactive


# no fucking clue why this won't inherit the ImageResource class correctly.
# driving me actually mad, fuck it for now.
class Player(Interactive):
    def __init__(self, file_name="", **kwargs):
        super().__init__(**kwargs)

        self.image = ImageResource(file_name)

    def key(self, key, keydown=False):
        self.image.set_key_down(key, keydown)

        if key == pl.K_w:
            self.set_y_vel((- self.g_vel) if keydown else 0)
        if key == pl.K_a:
            self.set_x_vel((- self.g_vel) if keydown else 0)
        if key == pl.K_s:
            self.set_y_vel(self.g_vel if keydown else 0)
        if key == pl.K_d:
            self.set_x_vel(self.g_vel if keydown else 0)

    def get_image(self):
        return self.image.get_image()

    def update(self, all_items=[]):
        self.image.next_frame()
        self.screen.blit(self.image.get_image(), self.get_position())
        super().update(all_items)

