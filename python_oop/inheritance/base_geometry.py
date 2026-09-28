#!/usr/bin/env python3
"""This module is to create BaseGeometry class"""

class BaseGeometry:
    """This class represents base geometry"""

    # Methods
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
