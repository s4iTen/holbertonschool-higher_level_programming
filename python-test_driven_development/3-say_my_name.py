#!/usr/bin/python3
"""this function print the first and the last name"""


def say_my_name(first_name, last_name=""):
    """and it raise an error if the type of the name is not a string """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
