#!/usr/bin/python3
"""Funtion add_attribute"""


def add_attribute(object, attr_name, value):
    """Adds a new attribute to an object if it's possible.

    parameters:
        object (__main__.MyClass): name of the object.
        attr_name ('str): name of the attribute.
        value (str): value of the attribute.

    Raises:
        TypeError:  if the object can’t have new attribute.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
