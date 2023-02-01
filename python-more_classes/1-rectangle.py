#!/usr/bin/python3
"""this is the documentathin of the class Rectangle"""


class Rectangle:
    """this is the main class function"""
    def __init__(self, width, height):
        self.height = height
        self.width = width

    """This is the method width"""
    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
