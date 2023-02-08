#!/usr/bin/python3
"""this is the declaration of the Module"""
import json


def from_json_string(my_str):
    """this module return an object represented by a JSON string"""
    return json.loads(my_str)
