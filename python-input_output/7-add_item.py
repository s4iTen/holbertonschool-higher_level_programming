#!/usr/bin/python3
import sys
"""
this function write the argv in JSON file

"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


cont = load_from_json_file('add_item.json')
save_to_json_file(cont, 'add_item.json')
for i in sys.argv[1:]:
    cont.append(i)
save_to_json_file(cont, 'add_item.json')
