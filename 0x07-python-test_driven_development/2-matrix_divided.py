#!/usr/bin/python3

"""This module works on the division of elements in a matrix """


def matrix_divided(matrix, div):
    """
    Division of elements
    """

    if not matrix(int, list) and not  isinstance(float, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

