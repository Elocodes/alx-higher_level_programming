#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """function returns the elements not common to both sets"""

    sets_union = set_1.symmetric_difference(set_2)
    return sets_union
