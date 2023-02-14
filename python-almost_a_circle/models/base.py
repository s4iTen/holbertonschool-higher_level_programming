#!/usr/bin/python3
"""this is the declaration of the class base"""


class Base:
    """
    this function assign the id to the self id
    or assign the public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id is None:
            self.id = Base.__nb_objects
        else:
            self.id = id
