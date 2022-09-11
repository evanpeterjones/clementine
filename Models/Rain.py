
#from Physics.Visible import Visible
from Models.GifResource import GifResource


class Rain(GifResource):
    def __init__(self, *args, **kwargs):
        super().__init__(filename="resources/Images/rain.gif", *args, **kwargs)

    def update(self, all_items=[]):
        self.render(self.screen, (50, 0))

    def key(self, key, keydown):
        pass