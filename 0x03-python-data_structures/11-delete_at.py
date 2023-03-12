#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """function deletes the item in my list whose index is given"""

    if idx < 0 or idx > len(my_list):
        return (my_list)
    else:
        for index, each_num in enumerate(my_list):
            if idx == index:
                del my_list[index]
        return (my_list)
