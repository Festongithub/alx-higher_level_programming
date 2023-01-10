#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
         """Method that calculates area of a rectangle"""

         return self.__width * self.__height

    def __str__(self):
         """Magic method to return a rectangle"""

         return "[Rectangle] {}/{}".format(self.__width, self.__height)
