#!/usr/bin/python3
"""A module that loads, adds and saves arguments to a Python list"""

import sys
import os.path

args = sys.argv[1:]

save_file = __import__("5-save_to_json_file").save_to_    json_file
load_file = __import__("6-load_from_json_file").load_from_json_file

json_list = []
if os.path.exists("./add_item.json"):
    json_list = load_from_json_file("add_item.json")

save_file(json_list + args, "add_item.json")
