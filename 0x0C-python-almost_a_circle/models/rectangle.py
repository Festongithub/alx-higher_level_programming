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

    @property
    def width(self):
        """
        return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets new value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        return height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets new value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        return x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets new value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x  must be > 0")
        self.__x = value

    @property
    def y(self):
        """
        return  value of y
        """
        return self.__width

    @y.setter
    def y(self, value):
        """
        sets new value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """
        Returns area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        that prints in stdout the Rectangle
        instance with the character #
        """

        if self.__y > 0:
            for y in range(self.__y):
                print()

                self.__y = 0

        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print("" * self.__x, end="")
                print("#", end="")
            print()

    def __str__(self):
        """
        overriding method
        """
        return ("[Rectangle] ({}){:d}/{:d} - {:d} / {:d}".format(self.id,
            self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Take arguments
        """
        if args is not None and len(args) != 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']

            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        d2 = {}
        d2['id'] = self.id
        d2['width'] = self.width
        d2['height'] = self.height
        d2['x'] = self.x
        d2['y'] = self.y
        return d2
