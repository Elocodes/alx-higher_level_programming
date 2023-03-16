#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """function returns the square of each int in matrix"""

    if matrix != []:
        matrix2 = matrix.copy()

        for i in range(len(matrix2)):
            matrix2[i] = list(map(lambda j: j**2, matrix2[i]))
        return matrix2
    else:
        return None
