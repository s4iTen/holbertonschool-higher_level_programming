#!/usr/bin/python3
"""this is the declaration of the class base"""


class base:
    """
    this function assign the id to the self id
    or assign the public instance attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        base.__nb_objects += 1
        if id is None:
            self.id =  base.__nb_objects
        else:
            self.id = id
