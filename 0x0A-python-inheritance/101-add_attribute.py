#!/usr/bin/python3

"""
This modules looks for addition of attributes
"""


def add_attribute(object, attr_name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
