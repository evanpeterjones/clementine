import pygame.locals as pl
import os

from Models.SpriteSheet import SpriteSheet


def get_pygame_key_from_character(kp_str: str = 'x'):
    if kp_str == 'w':
        return pl.K_w
    if kp_str == 'a':
        return pl.K_a
    if kp_str == 'd':
        return pl.K_d
    if kp_str == 's':
        return pl.K_s

    return pl.K_x


def parse_file_dsl(file_descriptor: str, sheet: list) -> dict:
    res = {}
    ''' another shitty thing I learned about Python, 
    if you call res.keys() inside the loop, it only calls this once
    and never again, for 'efficiency'
    bitch I want it to do what I tell it to do
    How about you just make your language better :?
    '''
    for i, keypress in enumerate(file_descriptor):
        res[get_pygame_key_from_character(keypress)] = [sheet[i]]
    for i, kp in enumerate(file_descriptor):
        res[get_pygame_key_from_character(kp)].append(sheet[i])

    return res


class ImageResource:
    def __init__(self, file_name: str = None, count_frames: int = 6, *args, **kwargs):

        self.ImageLoaded: bool = file_name is not None

        if self.ImageLoaded:
            self.NumFrames = len(file_name.split('.')[0].split(os.sep)[-1].split('_')[-1])
            file_list = file_name.split('.')[0].split(os.sep)[-1].split('_')
            self.Frames: dict = parse_file_dsl(file_list[1], SpriteSheet(file_name, self.NumFrames).load_strip())

        # Todo: this is borked if the player isn't accepting keyboard input, we need a whole ass other class for just
        #  AI objects with images and stuff
        self.FramePointer = 0
        self.FramesSinceUpdate = 0
        self.FramesBetweenUpdate = count_frames

        self.K_def = pl.K_s  # this needs to be like _ or something that isn't pressed often
        self.Key = self.K_def
        self.pressed = False

    def get_image(self):
        if self.ImageLoaded:
            return self.Frames[self.Key][self.FramePointer]

    def set_key_down(self, key, d):
        if self.ImageLoaded:
            self.FramePointer = 0
            if d:
                self.Key = key if (key in self.Frames.keys()) else self.K_def
            else:
                self.Key = self.K_def
            self.pressed = d

    def next_frame(self):
        self.FramesSinceUpdate += 1
        if self.ImageLoaded and self.FramesSinceUpdate >= self.FramesBetweenUpdate:
            self.FramesSinceUpdate = 0
            # Todo: fix this so it's not constantly cycling
            self.FramePointer = (self.FramePointer + 1) % len(self.Frames[self.Key])
