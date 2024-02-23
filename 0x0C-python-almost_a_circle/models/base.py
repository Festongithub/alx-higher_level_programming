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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns string representation of an object
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """

        json_file = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass

        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

            lists = cls.to_json_string(list_dic)

            with open(json_file, 'w') as f:
                f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string
        """

        if json_string is None or len(json_string) == 0:
            return []

        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        that returns an instance with all attributes already set:
        **dictionary can be thought of as a double pointer to a dictionary
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1,1)

        if cls.__name__== "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy
