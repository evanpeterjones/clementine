"""
base class must be implemented by anything to be displayed
Implements ImageResource so you can optionally provide an image

counter-intuitive for a base class, this could be done differently, but whatever
"""


class Visible:
    def __init__(self, x=0, y=0, x_vel=0, y_vel=0, x_acc=0, y_acc=0, term=10):

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

    def set_y_vel(self, yvel):
        self.y_vel = yvel

    def set_x_vel(self, xvel):
        self.x_vel = xvel

    def update(self):
        """progresses to next frame"""

        # Update Position
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

        if self.x_vel != 0 and abs(self.x_vel) < self.terminal:
            if self.x_vel > 0:
                self.x_vel += self.x_acc
            if self.x_vel < 0:
                self.x_vel -= self.x_acc

        if self.y_vel != 0 and abs(self.y_vel) < self.terminal:
            if self.y_vel > 0:
                self.y_vel += self.y_acc
            if self.y_vel < 0:
                self.y_vel -= self.y_acc

        # Update IMG to next character Frame
        #self.update_image()
