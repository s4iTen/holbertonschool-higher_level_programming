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

    @staticmethod
    def to_json_string(list_dictionaries):
        """this function retuen the json string representation of
         list_dictionaties"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this function writes a json representation
         of list_objs to a file"""
        print(cls.__name__)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            json_str = cls.to_json_string(dict_list)
            file.write(json_str)
