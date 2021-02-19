
from Models.Tile import Tile
from Physics.Visible import Visible


class Map(Visible):
    '''
    Class to dynamically create a tilemap and draw to screen
    By default should just make the edge of the screen the limits of motion
    Later would pull from either tilemaps, a file, or just always be generated dynamically
    '''
    def __init__(self, size=(1200,720), tile_size=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tile_map = [[Tile() for _ in range(size[1])] for _ in range(size[0])]
        # Todo: implement default walls, which should just be the size of the screen

    def update(self, all_items=[]):
        pass

    def key(self, key, keydown):
        pass