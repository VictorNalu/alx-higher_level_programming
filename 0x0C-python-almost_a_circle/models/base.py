#!/usr/bin/python3

"""Base model class"""


class Base:
    """base class for other classes"""

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Attribute:
            id (int. optional): identity of each instance.
            defaults to none.
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
