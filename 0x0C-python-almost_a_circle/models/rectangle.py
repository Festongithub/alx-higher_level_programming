#!/usr/bin/python3

"""
This module inherits from the Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    Inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instance of the Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Returns the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter that
        Modifies the value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Modifies the value of the width
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <  0:
            raise ValueError("height  must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Returns value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Modifies the value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x  must be >=  0")
        self.__x = value

    @property
    def y(self):
        """
        Returns value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Modifies the value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y  must be >= 0")
        self.__y = value
