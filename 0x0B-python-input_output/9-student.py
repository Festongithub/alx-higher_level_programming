#!/usr/bin/python3

"""
This module is Class oand JSON
"""


class Student:
    """
    A simple class rep for student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary of student
        """
        return self.__dict__
