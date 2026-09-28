#!/usr/bin/env python3
"""The module is for mixins"""


class SwimMixin:
    """This class represents swimming"""

    # Methods

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """This class represents flying"""

    # Methods
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """This class represents a flying fish"""

    def roar(self):
        print("The dragon roars!")


dragon = Dragon()
dragon.swim()
dragon.fly()
dragon.roar()
