import pygame

class Dialogue:
    def __init__(self):

        self.__pointer = 0
        self.script = ['“Are you sure you want me to tell you this? I’ve heard that the more you talk about it, the more likely it is for it to affect you?”']
        self.font = pygame.font.SysFont('arial', 24)
        self.img = self.font.render(self.script[self.__pointer], True, pygame.color.Color(255, 255, 255))

    def update(self, screen):
        screen.blit(self.img, (20, 20))
