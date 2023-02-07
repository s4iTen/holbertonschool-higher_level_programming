#!/usr/bin/python3
"""this is the class"""


class BaseGeometry:
    """this is the class content"""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(TypeError(f"{name} must be an integer"))
        if value <= 0:
            raise ValueError(ValueError(f"{name} must be greater than 0"))
