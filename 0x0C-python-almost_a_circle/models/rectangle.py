#!/usr/bin/python3
"""
Creates a Rectangle model
"""

from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base model"""

    # Private instance attributes:
    # __width -> width
    # __height -> height
    # __x -> x
    # __y -> y

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for instances of the class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Retrives the width of the rectangle

        Returns: width of rectangle(int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width

        Args:
            value(int): width of rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrives the height of the rectangle

        Returns: height of rectangle(int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height

        Args:
            value(int): height of rectangle

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Retrives x of the rectangle

        Returns: x of rectangle(int)
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x

        Args:
            value(int): x

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter y of the rectangle

        Returns: y of rectangle(int)
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout"""
        for _ in range(self.__height):
            print("#" * self.__width)
