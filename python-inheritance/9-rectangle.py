#!/usr/bin/python3
"""this is the declaration of the class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """this is the main module"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
         return "[Rectangle] {}/{}".format(self.__width, self.__height)
