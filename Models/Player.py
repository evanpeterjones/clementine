from Models.ImageResource import ImageResource
from Physics.Interactive import Interactive


# no fucking clue why this won't inherit the ImageResource class correctly.
# driving me actually mad, fuck it for now.
class Player(Interactive):
    def __init__(self, file_name="", **kwargs):
        super().__init__(**kwargs)

        self.image = ImageResource(file_name)

    def move(self, key_down, a, d):
        pass

    def get_image(self):
        return self.image.get_image()

    def update(self):
        self.image.next_frame()
        super().update()

