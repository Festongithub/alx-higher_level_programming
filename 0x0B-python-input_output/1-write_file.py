#!/usr/bin/python3

"""
writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    if filename:
        with open(filename, mode='w', encoding="utf-8")as f:
            num_of_char = f.write(text)
            return num_of_char
