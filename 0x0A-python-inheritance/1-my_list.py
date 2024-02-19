#!/usr/bin/python3

"""
a class MyList that inherits from list
"""


class MyList(list):
    """
    A simple class of myLit
    sorts a list in ascending order
    """
    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
