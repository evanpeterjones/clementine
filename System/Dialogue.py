import pygame
import pygame.freetype

class Dialogue:
    def __init__(self):

        self.__pointer = 0
        self.script = ['“Are you sure you want me to tell you this? I’ve heard that the more you talk about it, the more likely it is for it to affect you?”']
        self.font = pygame.font.SysFont('arial', 24)
        self.img = None
        self.font_size = 24
        #self.img = self.font.render(self.script[self.__pointer], True, )

    def initialize(self, font_type = 'resources/Freedom-10eM.tff'):
        #self.font = pygame.freetype.Font(font_type, self.font_size)
        #self.font = pygame.font.SysFont(font_type, self.font_size)
        self.img = self.font.render(self.get_dialogue(), True, pygame.color.Color(255, 255, 255))

    def get_dialogue(self):
        w, h = pygame.display.get_surface().get_size()
        start = self.script[self.__pointer]
        result = ''
        num_lines = len(self.script[self.__pointer]) / self.font_size


        return result

    def update(self, screen):
        if self.img is None:
            self.initialize()

        screen.blit(self.img, (20, 20))

