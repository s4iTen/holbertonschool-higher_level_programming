#!/usr/bin/python3
"""this is the declaration of the Module"""


def class_to_json(obj):
    """
    this function return a dictionary like representation of the object
    """
    return obj.__dict__
