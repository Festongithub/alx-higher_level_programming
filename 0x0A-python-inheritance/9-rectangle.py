#!/usr/bin/python3

"""
An empty class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """
        Creates an instance of a rectangle
        """
        self.__width = width
        self.__height = height

        # validate with integer_validator

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        calculates the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
