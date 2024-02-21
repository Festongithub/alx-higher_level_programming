#!/usr/bin/python3

"""
An empty class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from the BaseGeometry
    """
    def __init__(self, width, height):
        """
        Creates a new instance of a rectangle
        """
        self.__width = width
        self.__height = height

        # validate with integer_validator

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
