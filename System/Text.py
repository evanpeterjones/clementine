import pygame
import pygame.freetype
from Physics.Visible import Visible


class Text(Visible):
    def __init__(self, text="Close", font_type='resources/Freedom-10eM.tff', **kwargs):
        super().__init__(**kwargs)

        self.text = text
        self.font = pygame.font.SysFont(font_type, 24)
        #'arial'

        self.img = None
        self.initialize()

    def initialize(self):
        # self.font = pygame.freetype.Font(font_type, self.font_size)
        # self.font = pygame.font.SysFont(font_type, self.font_size)
        self.img = self.font.render(self.text, True, pygame.color.Color(255, 255, 255))

    def pos(self):
        return (pygame.display.get_surface().get_size()[0]/2,
                self.y_pos)

    def draw(self, screen):
        if self.img is None:
            self.initialize()

        screen.blit(self.img, self.pos())


class Dialogue:
    def __init__(self):
        self.__pointer = 0
        self.script = ["I had watched the flowerbeds"
                       "and every day they'd grown"
                       "until one day I woke"
                       "to find them buried in the snow"
                       "but that's the night I found him"
                       "with teeth that no blood knew"
                       "he sees the night and knows the sky"
                       "his crescent smile assumes"
                       "but now the crescent's looming"
                       "wider than his eyes"
                       "I see his lower half"
                       "it's peering through the blinds"
                       "and he's at the mail slot"
                       "up above the neck"
                       "he must have seen my looking"
                       "then never turned his back"]
        self.font = pygame.font.SysFont('arial', 24)
        self.img = None
        self.font_size = 24
        # self.img = self.font.render(self.script[self.__pointer], True, )

    def initialize(self, font_type='resources/Freedom-10eM.tff'):
        # self.font = pygame.freetype.Font(font_type, self.font_size)
        # self.font = pygame.font.SysFont(font_type, self.font_size)
        self.img = self.font.render(self.get_dialogue(), True, pygame.color.Color(255, 255, 255))

    def get_dialogue(self):
        w, h = pygame.display.get_surface().get_size()
        start = self.script[self.__pointer]
        result = ''
        num_lines = len(self.script[self.__pointer]) / self.font_size

        return result

    def update(self, all_items):
        if self.img is None:
            self.initialize()

        pygame.screen.blit(self.img, (20, 20))
