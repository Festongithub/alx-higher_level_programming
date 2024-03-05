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
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0

        self.width = width
        self.height = height
        self.x = x
        self.y = y
