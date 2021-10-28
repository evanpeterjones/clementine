import threading
import time

'''
Clock
singleton class for a multi-threaded clock!
author: Evan P Jones
'''


class Clock:
    """
    Initialize as you would any other class
      var = System.Clock()

    multi-threaded singleton allows global reference after instantiation in main
    """

    class __innerClock(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

            self.__fps = 60  # this might be set by a parameter later(?)
            self.__delta = round(1000 / self.__fps)
            self.__nextFrame = self.__time()
            self.__set_next_frame()

            # these represent the number of loops completed waiting for the next frame i.e. unused computation
            self.__averageFreeCycles = 0

        @staticmethod
        def __time():
            return int(round(time.time() * 1000))

        def __set_next_frame(self):
            self.__nextFrame += self.__delta

        def __update_cycles(self, cycles_this_frame):
            self.__averageFreeCycles = (self.__averageFreeCycles + cycles_this_frame) / 2

        # PUBLIC PROPERTIES

        def next_frame_ready(self):
            """
            Call at the end of a game loop after updating models before updating the display
            Tabulates the free computation cycles available at the end of each frame
            :return:
            """
            
            cycles = 0
            while self.__time() < self.__nextFrame:
                cycles += 1

            self.__set_next_frame()
            self.__update_cycles(cycles)

        @property
        def AverageCycles(self):
            return self.__averageFreeCycles

    instance = None

    def __new__(cls):
        """instantiate the timer, start the thread and return the current time"""
        if not Clock.instance:
            Clock.instance = Clock.__innerClock()
            Clock.instance.start()
        return Clock.instance
