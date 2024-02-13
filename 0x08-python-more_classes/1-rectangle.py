#!/usr/bin/python3

""" defines a rectangle by: (based on 0-rectangle.py) """


class Rectangle:
    def __init_(self, width=0, height=0):
        self.width = width
        self.height = height
    """
    Check for the width of the rectangle
    """
    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = value
    """
    Check for the height of the rectangle
    """
    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height
