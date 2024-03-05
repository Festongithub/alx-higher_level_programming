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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returns the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Modifies the value of the width
        """
        self.__width = width

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
        self.__height = height

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
        self.__y = value
