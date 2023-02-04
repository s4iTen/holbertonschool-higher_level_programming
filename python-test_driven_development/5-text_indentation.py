#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = ""
    for char in text:
        new += char
        if char in ['?', '.', ':']:
            new += '\n'
    print(new)
