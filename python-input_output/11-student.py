#!/usr/bin/python3
"""this is the declaration of the class student"""


class Student:
    """this is the main Module"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            return \
             {att: getattr(self, att) for att in attrs if hasattr(self, att)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
