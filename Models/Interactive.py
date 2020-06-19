'''
Base Class for all objects which can be interacted with
'''
from Models.Visible import Visible


class Interactive(Visible):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def collide(self):
        pass

    def reverse_x(self):
        pass

    def reverse_y(self):
        pass

