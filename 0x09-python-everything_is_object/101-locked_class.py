#!/usr/bin/python3

"""
Locked class
"""

class LockedClass:
    """No class or object attributes, can't set 
    except for First_name
    """
    def __setattr__(self,attributes, value):
        if  attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + attribute + "'")
