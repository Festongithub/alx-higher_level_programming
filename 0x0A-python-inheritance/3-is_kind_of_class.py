#!/usr/bin/python3

"""Returns true if the object of the instance is true """

def is_kind_of_class(obj, a_class):
    """Returns True if the object of instance or else false"""
    if type(obj) is a_class:
        return True 
    else:
        return False
