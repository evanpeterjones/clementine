"""
base class must be implemented by anything to be displayed
Implements ImageResource so you can optionally provide an 


counter-intuitive for a base class, this could be done differently, but whatever
"""


class Visible:
    def __init__(self, x=0, y=0, z=1, width=20, height=20, x_vel=0, y_vel=0, x_acc=0, y_acc=0, term=2, cursor=False, screen=None, **kwargs):
        super().__init__(**kwargs)

        # IF CURSOR_CONTROL_ENABLED
        self.cursor_control_enabled = cursor

        # SIZE
        self.width = width
        self.height = height

        # POSITION
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z # z index used for sorting elements in main before blit, so lower indexes display underneath higher indexes

        # VELOCITY
        self.x_vel = x_vel
        self.y_vel = y_vel

        # ACCELERATION
        self.x_acc = x_acc
        self.y_acc = y_acc

        # TERMINAL VELOCITY
        self.terminal = term
        # ^need to determine a good terminal velocity

        # SCREEN REFERENCE: IDK IF THIS IS A GOOD IDEA??
        self.screen = screen
        self.g_vel = 1

    def key(self, key, keydown=False):
        '''
        override this method in implementing class to handle what happens on keypresses
        '''
        pass

    def get_position(self):
        return [self.x_pos, self.y_pos]

    def set_position(self, position=(0, 0)):
        '''
        not meant to be used at all except on init, objects should be moved using velocity if possible
        :param x:
        :param y:
        :return:
        '''
        self.x_pos, self.y_pos = position

    def set_y_vel(self, yvel):
        self.y_vel = yvel

    def set_x_vel(self, xvel):
        self.x_vel = xvel

    def update(self, x_fric=0, y_fric=0, all_items=[]):

        # Update Position
        self.x_pos += (self.x_vel - x_fric)
        self.y_pos += (self.y_vel - y_fric)

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

    def contains(self, x, y):
        pass

    def draw(self):
        pass
