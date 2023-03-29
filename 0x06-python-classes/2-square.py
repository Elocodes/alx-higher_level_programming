#!/usr/bin/python3

class Square:
    """a class that attributes size to a square

    square: a four sided shape of which all sides are of equal length
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
