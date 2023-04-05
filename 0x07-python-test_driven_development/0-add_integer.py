#!/usr/bin/python3
"""This module adds two numbers.

The two numbers must be integers or floats. All floats are ccast into
integer before addition.
"""


def add_integer(a, b=98):
    """function adds two numbers.

    Args:
        param1(int): a
        param2(int): b

    Returns:
        Returns an integer, the addition of "a" and "b"
        """
    if type (a) is float:
        a = int(a)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return (a + b)


