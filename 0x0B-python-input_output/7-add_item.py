#!/usr/bin/python3
"""
This is a simple module and it only has
a script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = 'add_item.json'
items = []
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    save_to_json_file([], filename)

for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

save_to_json_file(items, filename)
