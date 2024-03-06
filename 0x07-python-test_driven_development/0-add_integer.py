#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers, casting them to integers if they are floats.
    Raises a TypeError if either argument is not an integer or float.
    Returns an integer
    """

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float):
        a = int(a)
        if isinstance(b, float):
            b = int(b)

            return a + b
