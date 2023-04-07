#!/usr/bin/python3
"""This module contains function that divides a matrix.

Each element of the matrix is divided and rounded to 2 decimal places.
The doctest for the function is contained in the file matrix_divided.txt.
"""


def matrix_divided(matrix, div):
    """function divides a matix.

    Args:
        param1(list): matrix is a list of lists of int or floats
        param2(int): divisor is an int or float

    Returns:
        Returns a new matrix of elements rounded to 2 decimal places
    """
    if matrix == [] or matrix is None:
        raise TypeError('matrix must be a matrix (list of lists)\
                of integers/floats')
    for item in matrix:
        if type(item) is not list:
            raise TypeError('matrix must be a matrix (list of lists)\
                    of integers/floats')
        for i in item:
            if type(i) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists)\
                        of integers/floats')
    column_check = len(matrix[0])
    for j in range(len(matrix)):
        if len(matrix[j]) != column_check:
            raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in [int, float] or div is None:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round(i/div, 2) for i in items] for items in matrix]
    return new_matrix
