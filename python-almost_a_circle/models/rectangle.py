#!/usr/bin/python3
"""this is the declaration of the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """this function call the super class base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
