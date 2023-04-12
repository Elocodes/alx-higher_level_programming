#!/usr/bin/python3

"""module demonstrates the use of builtin function.

The builtin function is used by the function to compare object type
"""


def inherits_from(obj, a_class):
    """function returns true if obj is an instance of a class
    that inherited from given class"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
