#!/usr/bin/python3
"""this is the class"""


class BaseGeometry:
    """this is the class content"""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(TypeError(f"{name} must be an integer"))
        if value == True or value == False:
            raise TypeError(TypeError(f"{name} must be an integer"))
        if value <= 0:
            raise ValueError(ValueError(f"{name} must be greater than 0"))
"""this is the declaration of the class Rectangle"""


class Rectangle(BaseGeometry):
    """this is the main module"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
