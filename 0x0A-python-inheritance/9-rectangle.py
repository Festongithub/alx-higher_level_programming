#!/usr/bin/python3


"""
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
(task based on 8-rectangle.py)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """
        Creates an instance of a rectangle
        """
        self.__width = width
        self.__height = height
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
