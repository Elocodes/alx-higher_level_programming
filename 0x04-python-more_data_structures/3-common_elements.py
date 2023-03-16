#!/usr/bin/python3

def common_elements(set_1, set_2):
    """function returns the element common to both sets"""

    list1 = list(set_1)
    list2 = list(set_2)
    list3 = []

    for i in list1:
        for j in list2:
            if i == j:
                list3.append(j)
    return list3
