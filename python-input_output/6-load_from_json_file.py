#!/usr/bin/python3
"""this is the declaration of the Moduel"""
import json


def load_from_json_file(filename):
    """this function load an object from Json file"""
    with open(filename, "r") as file:
        ret = json.load(file)
    return ret
