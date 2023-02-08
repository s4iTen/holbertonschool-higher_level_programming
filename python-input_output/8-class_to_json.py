#!/usr/bin/python3
"""this is the declaration of the module"""


def class_to_json(obj):
    """this function return a dictionary discription"""
    obj_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (int, float, str, bool)):
            obj_dict[attr] = value
        elif isinstance(value, list):
            obj_dict[attr] = [i for i in value]
        elif isinstance(value, dict):
            obj_dict[attr] = {key: value for key, value in value}
    return obj_dict
    