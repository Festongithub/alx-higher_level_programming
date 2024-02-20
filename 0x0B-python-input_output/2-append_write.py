#!/usr/bin/python3

"""
 appends a string at the end of a text file (UTF8)
 and returns the number of characters added
"""

def append_write(filename="", text=""):
    if filename:
        with open(filename, mode='a', encoding='utf-8') as f:
            chars_append = f.write(text)
            return chars_append
