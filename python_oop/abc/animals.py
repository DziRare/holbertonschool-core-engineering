#!/usr/bin/env python3
"""The module is for ABC"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """This class represents an abstract animal"""

    # Methods
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """This class represents an abstract animal"""

    # Methods
    def sound(self):
        return "Bark"


class Cat(Animal):
    """This class represents an abstract animal"""

    # Methods
    def sound(self):
        return "Meow"
