#!/usr/bin/python3

"""
A module for Integers
"""


class MyInt(int):
    """
    A class that inherits from the int
    """

    def __init__(self, value):
        """
        Instance of the class
        """
        self.__value = value

    def __eq__(self, other):
        """
        Checks for equal
        """
        return self.__value != other

    def __ne__(self, other):
        """
        check s for difference
        """
        return self.__value == other
