#!/usr/bin/python3

import math


class MagicClass:
    """
    MagicClass: A class that represents a magical shape.

    Attributes:
        __magic_radius (int or float): The magical radius of the shape.

    Methods:
        __init__(self, magic_radius=0): Initializes the MagicClass instance with a given magical radius.
        calculate_area(self): Calculates and returns the magical area of the shape.
        calculate_circumference(self): Calculates and returns the magical circumference of the shape.
    """

    def __init__(self, magic_radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            magic_radius (int or float): The magical radius of the shape.
                                         Defaults to 0.

        Raises:
            TypeError: If the provided magical radius is not a number.
        """
        if type(magic_radius) not in (int, float):
            raise TypeError('magic_radius must be a number')

        self.__magic_radius = magic_radius

    def calculate_area(self):
        """
        Calculates and returns the magical area of the shape.

        Returns:
            float: The magical area of the shape.
        """
        return self.__magic_radius ** 2 * math.pi

    def calculate_circumference(self):
        """
        Calculates and returns the magical circumference of the shape.

        Returns:
            float: The magical circumference of the shape.
        """
        return 2 * math.pi * self.__magic_radius

