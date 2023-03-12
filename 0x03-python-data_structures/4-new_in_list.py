#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """function replaces the item in my list whose index is given
    with new element while retaining both copies of list"""

    list_copy = my_list.copy()

    if idx < 0:
        return (list_copy)
    elif idx > len(my_list):
        return (list_copy)
    else:
        for index, each_num in enumerate(list_copy):
            if idx == index:
                list_copy[index] = element
                return (list_copy)
