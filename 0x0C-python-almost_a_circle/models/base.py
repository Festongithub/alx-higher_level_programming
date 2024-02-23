#!/usr/bin/python3

"""
This module describes the class  Base
this is a  modular representation for the whole
project
"""

import json


class Base:

    __nb_objects = 0

    """
    Class Representation of the base
    """

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

    def to_json_string(list_dictionaries):
        """
        Returns string representation of an object
        """
        list_dictionaries = {}

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)
