#!/usr/bin/python3
"""this is the documentathin of the class Rectangle"""


class Rectangle:
    """this is the main class function"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """This is the method width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if not self.__height or not self.__width:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
