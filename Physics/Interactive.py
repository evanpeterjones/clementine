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

    def collisions(self, all_items):
        '''
        we only want to call this when an object has moved
        Might implement a datastructure to make searching quicker
        for now just searches through all the positions
        '''
        for i in all_items:
            if i is self:
                continue
            if i.x_pos == self.x_pos and i.y_pos == self.y_pos:
                print("collision: "+str(i) +" "+str(self))
                return True
        return False

    def collide(self):
        self.x_vel = 0 #(-self.x_vel)
        self.y_vel = 0 #(-self.y_vel)

    def update(self, all_items, x_chg=0, y_chg=0, x_fric=0, y_fric=0):
        if self.collisions(all_items):
            self.collide()
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


