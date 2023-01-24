#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    char_C = "C"
    char_c = "c"
    for char in my_string:
        if char != char_C and char != char_c:
            new_list += char
    return new_list
