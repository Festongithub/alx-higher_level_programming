#!/usr/bin/python3

"""
This module describes the class  Base
this is a  modular representation for the whole
project
"""


class Base:

    """
    Class Representation of the base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instance of the class
        """
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

@staticmethod
def to_json_string(list_dictionaries):
    """returns the JSON string representation of list_dictionaries"""
    if list_dictionaries is None or list_dictionaries == "[]":
        return "[]"
    return json.dumps(list_dictionaries)
