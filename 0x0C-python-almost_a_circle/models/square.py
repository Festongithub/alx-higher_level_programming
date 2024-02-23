#!/usr/bin/python3

"""
This module imports the Rectangle model
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from the Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instance of the Rectangle-Square
        """
        super.__init__(id, x, y, width, height)
        self.size = 
        self.width = size
        self.height = size
