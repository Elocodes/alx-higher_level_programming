#!/usr/bin/python3
"""This module performs py operation on a rectangle

The class rectangle contains methods that calculate area
of the rectangle and ends up printing its current shape
on the stdout. a getter and setter property is employed
for getting and setting the current height and width of
the rectangle.
"""


class Rectangle:
    """An empty class that defines what a rectangle is.

    Rectangle: a four sided shape consisting of L and W
    of varying sizes.
    """
    def __init__(self, width=0, height=0):
        """function initializezs class attributes.

        Args:
            param1(int): Width of the rectangle
            param2(int): Height of the rectangle

        Returns:
            returns size of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """function gets the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """function sets the value of the private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """function gets the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """function sets the value of the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """function returns the area of a rectangle"""
        rect_area = self.__height * self.__width
        return rect_area

    def perimeter(self):
        """function returns the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            rect_perimeter = 0
        else:
            rect_perimeter = 2 * (self.__height + self.__width)
        return rect_perimeter
