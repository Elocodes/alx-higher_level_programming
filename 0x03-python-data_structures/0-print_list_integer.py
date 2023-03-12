#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """function prints each content of my list on a new line"""

    for each_item in my_list:
        print("{:d}".format(each_item))
