#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, returns False.
    """
    # Base case: If the object is an instance of the specified class, return True
    if obj.__class__ == a_class:
        return True
