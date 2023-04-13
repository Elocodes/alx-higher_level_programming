#!/usr/bin/python3

"""
This module demonstrates the use of python inheritance.
its test cases are contained base_geometry.txt
"""


class BaseGeometry():
    """This is the base class. it contain attributes that subsequent
    classes will inherit from.

    Arg: None
    """
    def area(self):
        """function raises an exception when area is called"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """function validates the value.

        value must be a positive integer.
        """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """class inherits from the base class BaseGeometry.

    Arg:
        BaseGeometry: the parentclass
    """
    def __init__(self, width, height):
        """function initializes the width and height of the rectangle

        Args:
            width(int) a private attribute
            height(int) a private attribute

        width and height must be validated by the integer validator function
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
