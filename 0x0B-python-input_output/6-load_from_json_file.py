#!/usr/bin/python3
"""A module containing the function, load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    parameter:
        filename (str): name of file.

    Returns: object.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
