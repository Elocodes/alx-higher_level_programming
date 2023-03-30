#!/usr/bin/python3
"""Use cases of python classes

This module contains a class which demonstrates how to set private
method attributes, and access it from another method. It demonstrates
the getter and setter methods too.
"""


class Square:
    """a class that attributes size to a square

    square: a four sided shape of which all sides are of equal length
    Area: size of square, squared
    """
    def __init__(self, size=0):
        """function initializes variables

        Args:
            param1: The first parameter

        Returns:
            returns size of the square

        """
        self.__size = size

    def area(self):
        """function returns area of square"""
        return (self.__size) ** 2

    @property
    def size(self):
        """function is a getter for the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """function sets the value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
