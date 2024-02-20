#!/usr/bin/python3
"""A module containing the function from_json_string"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    parameters:
        my_str (str): json object to convert to Python object.

    Returns:
        type: Python object.
    """

    return json.loads(my_str)
