#!/usr/bin/python3

"""
This  module inherits from the 9-rectangle.py
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """
        Instance of the square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        area implementation
        """
        return self.__size * self.__size
