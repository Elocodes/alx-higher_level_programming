#!/usr/bin/python3

def no_c(my_string):
    """function removes the c alphabet both capital and low case from a string
    and prints the rest"""

    new_str = ""

    for each_item in my_string:
        for i in each_item[:]:
            if i != 'c' and i != 'C':
                new_str += i
    return (new_str)
