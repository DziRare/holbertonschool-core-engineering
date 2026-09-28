#!/usr/bin/env python3
"""The module is for ABC"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """This class represents an abstract shape"""

    # Methods

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """This class represents a circle"""

    def __init__(self, radius):
        self.__radius = radius

    # Methods
    def area(self):
        return 3.14159 * (self.__radius**2)

    def perimeter(self):
        return 2 * 3.14159 * self.__radius


class Rectangle(Shape):
    """This class represents a rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # Methods
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * self.__width + 2 * self.__height


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
