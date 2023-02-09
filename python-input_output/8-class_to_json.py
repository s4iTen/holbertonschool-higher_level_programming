#!/usr/bin/python3
"""this is the declaration of the Module"""


def class_to_json(obj):
    """
    this function return a dictionary like representation of the object
    """
    if isinstance(obj, (int, float, str, bool)):
        return obj
    elif isinstance(obj, list):
        for item in obj:
            return class_to_json(item)
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, object):
        obj_dict = {}
        for attr, value in obj.__dict__.items():
            obj_dict[attr] = class_to_json(value)
        return obj_dict
    else:
        i = (type(obj).__name__)
        raise TypeError(f"Object of type '{i}' is not JSON serializable")
