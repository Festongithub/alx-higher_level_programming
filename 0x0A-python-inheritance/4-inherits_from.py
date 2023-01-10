#!/usr/bin/python3

def inherits_from(obj, a_class):
        # check if the object is an instance of a class that inherited from the specified class
        if type(obj) is a_class or not isinstance(obj, a_class):
            return False
        else:
            return True
