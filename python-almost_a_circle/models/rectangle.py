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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value

    def area(self):
        """this function return the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """this function display the rectangle"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        h = self.__height
        w = self.__width
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {w}/{h}")

    def update(self, *args):
        """
        this function assign the arguments of it
         to the argument of the main function
        """
        arg_count = len(args)
        if arg_count > 0:
            self.id = args[0]
        if arg_count > 1:
            self.width = args[1]
        if arg_count > 2:
            self.height = args[2]
        if arg_count > 3:
            self.x = args[3]
        if arg_count > 4:
            self.y = args[4]
