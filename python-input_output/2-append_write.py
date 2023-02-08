#!/usr/bin/python3
"""this is the declaration of the module"""


def append_write(filename="", text=""):
    """this Module open the file and write in it"""
    with open(filename, 'a', encoding='utf8') as f:
        f.write(text)
    f.close()
    return len(text)
