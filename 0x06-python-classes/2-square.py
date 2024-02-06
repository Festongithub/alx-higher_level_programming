#!/usr/bin/python3

""" Defines a class Square """


class Square:
    """
    with an attribute of size """
    def __init__(self, size=0):
        """ Size is private instance attribute """
        self.__size = size
    if not  isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size
