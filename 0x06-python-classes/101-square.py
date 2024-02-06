#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 2-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeErro("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ that returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for j in range(self.__position[1]):
            print()
            for i in range(self.__size):
                print()
                for k in range(self.__position[0]):
                    print(" ", end="")
                    print("#" * self.__size)

    def __str__(self):
        """Prints square offsetting it by position with symbol #

        Returns: The square.
        """
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for e in range(self.size))
