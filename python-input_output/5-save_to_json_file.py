#!/usr/bin/python3
"""this is the declaration of the Module"""
import json


def save_to_json_file(my_obj, filename):
    """this function write an Object in a JSON file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
