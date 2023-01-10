#!/usr/bin/python3

"""Look up"""

def lookup(obj):
    """Get the list of attributes and methods of the object"""
    attributes = dir(obj)
    """Return attributes"""
    return attributes
