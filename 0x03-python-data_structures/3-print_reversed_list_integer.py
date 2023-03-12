#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function prints the reverse of each content of my list on a new line"""
    if not my_list:
        return (None)

    my_list.sort(reverse=True)

    for each_item in my_list:
        print("{:d}".format(each_item))
