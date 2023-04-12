#!/usr/bin/python3

"""module demonstrates the use of builtin function.

The builtin function is used by the function to compare object type
"""


def is_same_class(obj, a_class):
    """function returns true if obj is exactly an instance of given class"""
    if type(obj) is a_class:
        return True
    else:
        return False
