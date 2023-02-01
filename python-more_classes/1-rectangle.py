#!/usr/bin/python3
"""this is the documentathin of the class Rectangle"""


class Rectangle:
    """this is the main class function"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    """This is the method width"""
    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
