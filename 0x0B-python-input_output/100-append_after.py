#!/usr/bin/python3

"""
A module that adds text in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r") as f:
        message = f.readlines()

    with open(filename, "w") as fo:
        i = ""

        for line in message:
            i += line
            if search_string in line:
                i += new_string
        fo.write(i)
