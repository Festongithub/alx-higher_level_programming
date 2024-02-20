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
    if obj.__class__ == a_class:
        return True
