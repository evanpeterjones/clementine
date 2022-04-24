import pygame.locals as pl

from Models.ImageResource import ImageResource
from Physics.Interactive import Interactive


# had no clue why this wouldn't inherit the ImageResource class correctly.
# turns out, with multiple inheritance, you have to provide the keyword arguments
# explicitly, which I think is why it was not initializing properly
class Player(Interactive, ImageResource):
    def __init__(self, file_name=None, **kwargs):
        super().__init__(file_name=file_name, **kwargs)
        # may be more efficient to manually init both parent classes
        # not sure

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

