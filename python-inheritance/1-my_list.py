#!/usr/bin/python3
"""this is the class MyList"""


class MyList(list):
    """this module print sorted list"""
    def print_sorted(self):
        print(sorted(self))
