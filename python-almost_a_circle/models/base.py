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
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            dict_list = []
            if list_objs is not None:
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
            json_str = cls.to_json_string(dict_list)
            file.write(json_str)

    def from_json_string(json_string):
        """This function returns a list of the JSON string representation"""
        if json_string:
            if isinstance(json_string, list):
                return json_string
            else:
                res = json.loads(json_string)
                return res
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        This method returns a new instance of the class
        with the specified attributes.
        """
        if cls.__name__ == "Rectangle":
            res = cls(1, 1)
        if cls.__name__ == "Square":
            res = cls(1)
        res.update(**dictionary)
        return res

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a file in JSON format"""
        try:
            file = cls.__name__ + ".json"
            with open(file, "r") as f:
                json_data = f.read()
                dict_list = cls.from_json_string(json_data)
                obj_list = [cls.create(**d) for d in dict_list]
                return obj_list
        except FileNotFoundError:
            return []
