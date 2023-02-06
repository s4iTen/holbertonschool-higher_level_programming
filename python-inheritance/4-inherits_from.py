#!/usr/bin/python3
"""this is the Module"""


def inherits_from(obj, a_class):
    """this module check if obj is instance od class or not"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
