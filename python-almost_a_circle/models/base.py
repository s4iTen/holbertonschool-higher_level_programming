#!/usr/bin/python3
"""this is the declaration of the class base"""
import json


class Base:
    """
    this function assign the id to the self id
    or assign the public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """this function retuen the json string representation of
         list_dictionaties"""
        return json.dumps(list_dictionaries)
