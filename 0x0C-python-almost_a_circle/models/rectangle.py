#!/usr/bin/python3

"""
This module of rectangle inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Inherits from The Class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class construct and instance
        """
        super().__init__(id)
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)

        def get_width(self):
            """
            gets the width value
            """
            return self.__width

        def set_width(self, width):
            """
            sets new value of width
            """
            if not isinstance(width, int):
                raise TypeError("width must be an integer")

            if width <= 0:
                raise ValueError("width  must be > 0")
            self.__width = width

        def get_height(self):
            """
            gets the value of the height
            """
            return self.__height

        def set_height(self, height):
            """
            Returns new value of height
            """
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            # height validation
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height

        def get_x(self):
            """
            Returns the value of x
            """
            return self.__x

        def set_x(self, x):
            """
            set new value of x
            """

            if not isinstance(x, int):
                raise TypeError("x must be an integer")

            # x validation
            if x < 0:
                raise ValueError("x must be > 0")

            self.__x = x

        def get_y(self):
            """
            Returns new value of y
            """
            return self.__y

        def set_y(self, y):
            """
            Returns new value of y
            """

            if not isinstance(y, int):
                raise TypeError("y must be an integer")

            if y < 0:
                raise ValueError("y must be > 0")
            self.__y = y
