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

        attrs = ["id", "size", "x", "y"]
        if args:
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """Override the __str__method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
