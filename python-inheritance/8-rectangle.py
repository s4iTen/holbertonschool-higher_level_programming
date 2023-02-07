#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""this is the declaration of the class"""


class Rectangle (BaseGeometry):
    """this is the main module"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
