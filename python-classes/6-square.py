#!/usr/bin/python3
"""Define a Class Square"""


class Square:
    """Represent Square"""
    def __init__(self, size=0,position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value=0):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size > 0:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for i in range(self.size):
                if self.__position[0] > 0:
                    for i in range(self.__position[0]):
                        print(" ", end="")
                for i in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
