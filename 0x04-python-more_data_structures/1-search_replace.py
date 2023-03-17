#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """function replaces int elements in found in search in my list"""

    if my_list == []:
        return ([])
    else:
        list2 = my_list.copy()
        for i in range(len(list2)):
            if list2[i] == search:
                list2[i] = replace
        return (list2)
