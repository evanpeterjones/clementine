

from Physics.Fundamental import Direction, Force

"""
Class to represent the force of Gravity to act on all objects
 
Should be inherited by all Interactive Elements. 
"""


class Gravity:
    class __innerGravity(Direction, Force):
        def __init__(self, *args, **kwargs):
            super().init(*args, **kwargs)

    instance = None

    def __new__(cls):
        """instantiate global gravity"""
        if not Gravity.instance:
            Gravity.instance = Gravity.__innerGravity()

        return Gravity.instance
