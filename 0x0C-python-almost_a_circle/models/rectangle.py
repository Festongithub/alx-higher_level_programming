#!/usr/bin/python3

"""Define the class rectangle"""


from models.base import Base


class Rectangle(Base):
    """The class inherits from the class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The class instantiation"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for the height"""
        if not isinstance(value, int):
            raise TypeError("height  must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the value of the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for the x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the value of the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Property setter for the y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance
        area is given as width  by height
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
