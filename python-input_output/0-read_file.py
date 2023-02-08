#!/usr/bin/python3
"""this is the definition of the function"""


def read_file(filename=""):
    """this Module open the file and read it"""
    f = open(filename, 'r')
    print(f.read())
    f.close()
