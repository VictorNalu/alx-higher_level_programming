#!/usr/bin/python3
"""A module that loads, adds and saves arguments to a Python list"""

from sys import argv

args = argv[1:]

save_file = __import__("5-save_to_json_file").save_to_json_file
load_file = __import__("6-load_from_json_file").load_from_json_file

try:
    json_list = load_file("add_item.json")
except (ValueError, FileNotFoundError):
    json_list = []

json_list.extend(args)

save_file(json_list, "add_item.json")
