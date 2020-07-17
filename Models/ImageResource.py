from resources.Colors import FG

import pygame
import os

F_IMG_ERROR = "none_img_1.png"

class SpriteSheet:
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except:
            print("file not found: " + filename)

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey=None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey=None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

class ImageResource:
    def __init__(self, file_name: str = F_IMG_ERROR, *args, **kwargs):
        self.image_count = int(file_name.split('.')[0].split(os.sep)[-1].split('_')[-1])
        self.sheet = SpriteSheet(file_name)
        self.Frames = self.sheet.load_strip((), self.image_count)
        self.FramePointer = 0
        self.NumFrames = 1

        # self.Frames.append(
        self.img = pygame.image.load(os.path.join('resources', file_name))

        if self.img is not None:
            self.sheet = self.img.convert()
            rect = self.sheet.get_rect().size

            if self.sheet is not None:
                self.Frames = self.__load_strip(rect, self.image_count)
                self.NumFrames = len(self.Frames)

    def get_image(self):
        return self.Frames[self.FramePointer]

    def __image_at(self, rectangle, colorkey):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        # image.blit(self.sheet, (0,0), rect)

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def __images_at(self, rects, colorkey):
        "Loads multiple images, supply a list of coordinates"
        return [self.__image_at(rect, colorkey) for rect in rects]

    def __load_strip(self, rect: tuple, image_count: int, colorkey=None):
        "Loads a strip of images and returns them as a list"
        width = rect[0] / image_count
        tups = [(width * x, rect[1], width, rect[1]) for x in range(image_count)]
        return self.__images_at(tups, colorkey)


''''