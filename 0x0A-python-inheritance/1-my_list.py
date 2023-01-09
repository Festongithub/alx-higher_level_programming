#!/usr/bin/python3

class MyList(list):
    """Contains a list """
    def print_sorted(self):
        """Prints self in assorted format"""
        print(sorted(self))
