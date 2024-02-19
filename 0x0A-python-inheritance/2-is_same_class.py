#!/usr/bin/python3

"""
Returns true or False
"""


def is_same_class(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is a_class
