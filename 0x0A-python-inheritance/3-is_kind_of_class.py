#!/usr/bin/python3

"""module demonstrates the use of builtin function.

The builtin function is used by the function to compare object type
"""


def is_kind_of_class(obj, a_class):
    """function returns true if obj is an instance of given class
    or instance of a class that inherited from given class"""
    return (isinstance(obj, a_class))
