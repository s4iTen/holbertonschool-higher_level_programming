#!/usr/bin/python3
"""this is the declaration of the class Square"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """this is the main method"""
    def __init__(self, size):
        self.__size = size
        Rectangle.integer_validator(self, 'size', size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
