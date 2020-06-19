from enum import Enum

from Models.Interactive import Interactive


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Player(Interactive):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move(self, direction):
        pass
