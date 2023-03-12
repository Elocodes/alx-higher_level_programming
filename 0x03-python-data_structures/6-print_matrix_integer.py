#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """function prints a list embedded in another list"""
    if matrix == []:
        return (None)
    else:
        for each_list in matrix:
            for i in each_list:
                print("{} ".format(i), end='')
            print()
