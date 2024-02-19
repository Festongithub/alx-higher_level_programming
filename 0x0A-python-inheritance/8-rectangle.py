#!/usr/bin/python3

"""
An empty class
"""


class BaseGeometry:

    """
    Class called BaseGeometry
    """

    def area(self):
        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        # validate with integer_validator

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
