#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""this is the declaration of the Module"""


cont = load_from_json_file('add_item.json')
save_to_json_file(cont, 'add_item.json')
"""
this cont is the list that we are going to load in the json file
"""
for i in sys.argv[1:]:
    cont.append(i)
save_to_json_file(cont, 'add_item.json')
