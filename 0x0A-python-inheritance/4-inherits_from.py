#!/usr/bin/python3
"""Inherits from"""

def inherits_from(obj, a_class):
    """Function returns direct or indirectly"""
    if type(obj) is a_class: 
        return False
    else:
        return True
