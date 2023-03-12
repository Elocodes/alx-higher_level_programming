#!/usr/bin/python3

def max_integer(my_list=[]):
    """function returns the biggest integer of a list"""

    if my_list == []:
        return (None)
    else:
        my_list.sort(reverse=True)
        return (my_list[0])
