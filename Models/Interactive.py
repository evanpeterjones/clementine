'''
Base Class for all objects which can be interacted with
'''
from Physics.Visible import Visible


class Interactive(Visible):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def collide(self):
        pass

    def reverse_x(self):
        pass

    def reverse_y(self):
        pass

