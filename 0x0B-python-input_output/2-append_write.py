#!/usr/bin/python3

"""
A module for appending text to a file
"""


def append_write(filename="", text=""):
    """
    Appends text
    """
    with open(filename, 'a', encoding="utf-8") as f:
        num_char = f.write(text)
        return num_char
