"""
base class must be implemented by anything to be displayed
"""


class Visible:
    def __init__(self, img=None, x=0, y=0, x_vel=0, y_vel=0, x_acc=0, y_acc=0, term=10):
        # VISIBLE COMPONENT
        self.img = img # these are created with pygame.image.load('''resource file-path''')
        # might implement the visible component as its own class so you can cycle to the next frame programmatically

        # POSITION
        self.x_pos = x
        self.y_pos = y

        # VELOCITY
        self.x_vel = x_vel
        self.y_vel = y_vel

        # ACCELERATION
        self.x_acc = x_acc
        self.y_acc = y_acc

        # TERMINAL VELOCITY
        self.terminal = term
        # ^need to determine a good terminal velocity

    def get_position(self):
        return [self.x_pos, self.y_pos]

    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def update(self):
        """progresses to next frame"""

        # Update Position
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

        # Update Velocity
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc

        # Update IMG to next character Frame