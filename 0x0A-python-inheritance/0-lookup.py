#!/usr/bin/python3

"""This module contains a function returning a list.

function returns all the attributes and methods of an object
"""


def lookup(obj):
    """function returns the attributes and methods of obj"""

    the_list = dir(obj)
    return the_list
