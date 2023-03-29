#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """function prints the items in a dict sorted alphabeticaly"""

    """for key in a_dictionary.items():
        if not isinstance(key, dict):"""
    dict2list = sorted(a_dictionary.items())
    sorted_dict = dict(dict2list)

    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))
