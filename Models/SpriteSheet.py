import pygame
import os


class SpriteSheet:
    def __init__(self, filename="none_img_1.png", image_count=1):
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
                if colorkey == -1:
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
