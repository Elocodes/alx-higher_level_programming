#!/usr/bin/python3
"""Use cases of python classes

This module contains a class which demonstrates how to set private
method attributes, and access it from another method. It demonstrates
the getter and setter methods too.
"""


class Square:
    """a class that attributes size to a square

    square: a four sided shape of which all sides are of equal length
    """
    def __init__(self, size=0):
        """function initializes variables

        Args:
            param1: The first parameter

        Returns:
            returns size of the square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
