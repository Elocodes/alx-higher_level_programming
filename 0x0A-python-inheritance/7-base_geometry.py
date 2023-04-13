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
