'''
Base Class for all objects which can be interacted with
'''
from Physics.Visible import Visible

class Interactive(Visible):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def no_collisions(self, all_items):
        '''
        we only want to call this when an object has moved
        Might implement a datastructure to make searching quicker
        for now just searches through all the positions
        '''
        for i in all_items:
            if i.x_pos == self.x_pos and i.y_pos == self.y_pos:
                print('collision')
                return False
        return True

    def update(self, x_chg=0, y_chg=0, x_fric=0, y_fric=0, all_items=[]):
        if self.no_collisions(all_items):
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


    def reverse_x(self):
        pass

    def reverse_y(self):
        pass

