#!/usr/bin/python3

def element_at(my_list, idx):
    """function returns the element in my list whose index is given"""
    if idx < 0:
        return (None)
    elif idx > len(my_list):
        return (None)
    else:
        for index, each_num in enumerate(my_list):
            if idx == index:
                return (each_num)
