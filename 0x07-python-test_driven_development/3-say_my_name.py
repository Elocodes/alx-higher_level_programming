#!/usr/bin/python3
"""This module prints names to stdout.

The function accepts two arguments, first and last names which must be strings
"""


def say_my_name(first_name, last_name=""):
    """function prints first name only or first and last(if passed)

    Args:
        param1(str): first name
        param2(str): last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
