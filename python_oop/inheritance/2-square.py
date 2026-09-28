#!/usr/bin/env python3
"""This module is to create Square class"""

Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """This class represents a square"""

    # Initialisation
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    # Methods
    def area(self):
        return self.__size**2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
