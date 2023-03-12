#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """function replaces the item in my list whose index is given
    with new element"""

    if idx < 0:
        return (my_list)
    elif idx > len(my_list):
        return (my_list)
    else:
        for index, each_num in enumerate(my_list):
            if idx == index:
                my_list[index] = element
        return (my_list)
