#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from sys import argv
    args = sys.argv[1:]
    result = sum(int(arg) for arg in args)
    print(result)
