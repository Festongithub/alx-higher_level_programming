#!/usr/bin/python3

def read_file(filename=""):
    """
    reads a text file 
    """
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
