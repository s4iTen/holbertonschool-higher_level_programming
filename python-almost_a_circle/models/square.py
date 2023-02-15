#!/usr/bin/python3
"""this is the declaration of the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is the main function"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.__height = value
        self.width = value

    def __str__(self):
        """this is the Str function"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
