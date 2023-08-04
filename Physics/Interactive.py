'''
Base Class for all objects which can be interacted with
'''
from Physics.Visible import Visible


class Interactive(Visible):
    '''
    the main difference between this class and the Visible class is that this
    adds the default collision logic which will just loop through all of the
    elements on screen and check for collision on each update
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bounce = 2

    def contains(self, x, y):
        '''check to see if a point exists inside bounds of self
        this assumes the shape of the self to be a square
        it should be overridden in non-square classes'''
        return (self.x_pos <= x <= (self.x_pos + self.width) and
                self.y_pos <= y <= (self.y_pos + self.height))

    def collisions(self, all_items):
        '''
        we only want to call this when an object has moved
        Might implement a datastructure to make searching quicker
        for now just searches through all the positions
        '''
        collision = False
        for i in all_items:
            "only compare the bounds in the direction we're moving"
            if i is self:
                continue

            if self.x_vel > 0:
                # compare against our right bounds
                if i.contains(self.x_pos + self.width, self.y_pos) or \
                   i.contains(self.x_pos + self.width, self.y_pos + self.height):

                    self.right_collision()
                    collision = True
            else:
                # compare against right bounds of other object
                if i.contains((self.x_pos + self.width), self.y_pos) or \
                   i.contains((self.x_pos + self.width), (self.y_pos + self.height)):

                    self.right_collision()
                    collision = True
            if self.y_vel > 0:
                # compare against upper bounds of other object
                if i.contains(self.x_pos, self.y_pos) or \
                   i.contains(self.x_pos + self.width, self.y_pos):

                    self.top_collision()
                    collision = True
            else:
                # compare against lower bounds of other object
                if i.contains(self.x_pos, self.y_pos + self.height) or \
                   i.contains(self.x_pos + self.width, self.y_pos + self.height):

                    self.bottom_collision()
                    collision = True

        if collision:
            self.on_collision(all_items)

        return collision

    def bottom_collision(self):
        self.y_vel = 0
        self.y_pos = self.y_pos - (self.bounce * self.y_vel)

    def top_collision(self):
        self.y_vel = 0
        self.y_pos = self.y_pos - (self.bounce * self.y_vel)

    def left_collision(self):
        self.x_pos = self.x_pos - (self.bounce * self.x_vel)
        self.x_vel = 0

    def right_collision(self):
        self.x_pos = self.x_pos - (self.bounce * self.x_vel)
        self.x_vel = 0

    def on_collision(self, all_items=[]):
        pass

    def update(self, all_items, x_chg=0, y_chg=0, x_fric=0, y_fric=0):
        if self.collisions(all_items):
            self.on_collision(all_items=all_items)
        else:
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