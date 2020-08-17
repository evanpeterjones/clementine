from resources.Colors import FG

import pygame
import os

F_IMG_ERROR = "none_img_1.png"


class SpriteSheet:
    def __init__(self, filename=F_IMG_ERROR, image_count=1):
        try:
            self.image_count = image_count
            self.sheet = pygame.image.load('resources' + os.path.sep + filename).convert()
            self.dimensions = (self.sheet.get_size()[0] / self.image_count, self.sheet.get_size()[1])

        except:
            print("file not found: " + filename)

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey=None):
        "Loads image from x,y,x+offset,y+offset"
        if self.sheet is not None:
            rect = pygame.Rect(rectangle)
            image = pygame.Surface(rect.size).convert()
            image.blit(self.sheet, (0, 0), rectangle)
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey, pygame.RLEACCEL)
            return image
        return None

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey=None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, colorkey=None):
        "Loads a strip of images and returns them as a list"
        tups = [(self.dimensions[0] * x, 0, self.dimensions[0], self.dimensions[1])
                for x in range(self.image_count)]
        return self.images_at(tups, colorkey)


def parse_file_dsl(file_descriptor: str, sheet: list) -> dict:
    res = {}
    for i, keypress in enumerate(file_descriptor):
        if keypress in res.keys():
            res[keypress].append(sheet[i])
        else:
            res[keypress] = [sheet[i]]
    return res


class ImageResource:
    def __init__(self, file_name, count_frames: int = 6, * args, **kwargs):

        self.NumFrames = len(file_name.split('.')[0].split(os.sep)[-1].split('_')[-1])
        file_list = file_name.split('.')[0].split(os.sep)[-1].split('_')
        self.Frames: dict = parse_file_dsl(file_list[1], SpriteSheet(file_name, self.NumFrames).load_strip())
        self.FramePointer = 0
        self.FramesSinceUpdate = 0
        self.FramesBetweenUpdate = count_frames

        self.KeyDown = 'w'

    def get_image(self):
        # self.next_frame()
        return self.Frames[self.KeyDown][self.FramePointer]

    def ready_next(self):
        self.FramesSinceUpdate += 1

        if self.FramesSinceUpdate >= self.FramesBetweenUpdate:
            self.FramesSinceUpdate = 0
            return True
        return False

    def next_frame(self):
        if self.ready_next():
            self.FramePointer = (self.FramePointer + 1) % len(self.Frames[self.KeyDown])

    def set_key_down(self, key='-', update = False):
        self.KeyDown = key
        if update:
            # honestly don't know how I'm going to do this in the end
            self.FramePointer = 0

'''
realized file_names should 
'''
# sswsddddddddxxxxww
