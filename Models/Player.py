from Models.ImageResource import ImageResource
from Models.Interactive import Interactive
import os

# no fucking clue why this won't inherit the ImageResource class correctly.
# driving me actually mad, fuck it for now.
class Player(Interactive, ImageResource):
    def __init__(self, file_name, **kwargs):
        super().__init__(**kwargs)

        self.image = ImageResource(file_name)

    def move(self, direction, a, d):
        pass

    def get_image(self):
        return self.image.get_image()


