#!/usr/bin/python3

class Square:
    """a class that attributes size to a square

    square: a four sided shape of which all sides are of equal length
    Area: size of square, squared
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("".join(["#" for j in range(self.__size)]))

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
