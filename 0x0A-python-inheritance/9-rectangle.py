#!/usr/bin/python3

"""
An empty class
"""

BaseGeometry = __import__('8-rectangle').BaseGeometry


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
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width} / {self.__height}"

    def __repr__(self):
        return f"[Rectangle] {self.__width} / {self.__height}"
