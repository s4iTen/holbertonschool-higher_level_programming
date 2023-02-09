#!/usr/bin/python3
"""this is the declaration of the class student"""


class Student:
    """this is the main Module"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
