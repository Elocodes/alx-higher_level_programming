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
    def __init__(self, size=0, position=(0, 0)):
        """function initializes variables

        Args:
            param1(int): The first parameter
            param2(tuple): the second parameter

        Returns:
            returns size of the square

        """
        self.__size = size
        self.__position = position

    def area(self):
        """function calculates the area of a square

        Args:
            param1(int): size of the square

        Returns:
            returns area of the square

        """
        return (self.__size) ** 2

    def my_print(self):
        """function prints the square's shape using #

        Args:
            param1: size
            param2: position

        Returns:
            None

        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    @property
    def size(self):
        """function is a getter for the private attribute size

        Args:
            param1: size

        Returns:
            the size of the square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """function sets the value for size

        Args:
            param1: value

        Returns:
            the current value of square

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """function is a getter for the private attribute position"""
        return self.__position

    @size.setter
    def position(self, value):
        """function sets the value for position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] <= 0 or value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
