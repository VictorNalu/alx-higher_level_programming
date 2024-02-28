#!/usr/bin/python3
"""Defines a class Basemodel"""


class Base:
    """Base class model for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
