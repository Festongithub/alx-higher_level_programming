#!/usr/bin/python3

"""
Writes a file in stdup
"""


def read_file(filename=""):
    if filename:
        with open(filename, mode="r", encoding="utf-8") as f:
            for line in f:
                print(line, end="")
