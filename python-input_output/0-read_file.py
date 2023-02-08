#!/usr/bin/python3
"""this is the definition of the function"""


def read_file(filename=""):
    """this Module open the file and read it"""
    with open(filename, 'r', encoding='utf8') as f:
        file = f.read()
        print(file, end="")
    f.close()
