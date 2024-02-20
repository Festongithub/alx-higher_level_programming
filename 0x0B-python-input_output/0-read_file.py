#!/usr/bin/python3

"""
Writes a file in stdup
"""


def read_file(filename=""):
    with open(filename,"r", encoding="UTF-8") as f:
        print(f.read(), end="")
