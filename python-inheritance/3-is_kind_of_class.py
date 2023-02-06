#!/usr/bin/python3
"""this is the Module"""


def is_kind_of_class(obj, a_class):
    """this module check if obj is instance od class or not"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
