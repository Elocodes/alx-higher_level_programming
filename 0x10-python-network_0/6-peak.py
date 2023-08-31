#!/usr/bin/python3

"""
technical interview prep ques
"""


def find_peak(list_of_integers):
    """function finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    return max(list_of_integers)
