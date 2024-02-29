#!/usr/bin/python3
"""
A class for Square model"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialise a new square"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args:
            # If positional arguments exist, update attributes based on their order
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            # If no positional arguments, update attributes based on keyword arguments
            if "size" in kwargs:
                self.size = kwargs["size"]
            else:
                raise ValueError("Size must be provided")
            for key, value in kwargs.items():
                if key != "size":
                    if hasattr(self, key):
                        setattr(self, key, value)
                    else:
                        raise TypeError(f"Invalid attribute: {key}")

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """Override the __str__method"""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"
