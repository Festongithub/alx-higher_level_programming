#!/usr/bin/python3

"""
This module checks for object and  classes
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise,
    returns False.
    """
    # Base case
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
