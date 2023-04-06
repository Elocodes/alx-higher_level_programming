#!/usr/bin/python3
"""This module performs py operation on a rectangle

The class rectangle contains methods that calculate area
of the rectangle and ends up printing its current shape
on the stdout. a getter and setter property is employed
for getting and setting the current height and width of
the rectangle.
"""


class Rectangle:
    """A class that defines what a rectangle is.

    Rectangle: a four sided shape consisting of L and W
    of varying sizes.
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """function returns the shape of the rectangle using the symbol '#'"""
        rect_shape = ""
        if self.__width != 0 or self.__height != 0:
            rect_shape += '\n'.join(str(self.print_symbol) * self.__width
                                    for row in range(self.__height))
        return rect_shape

    def __repr__(self):
        """function returns string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """function prints statement if rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """function returns the rectangle whose area is bigger"""
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """function returns a square"""
        return cls(size, size)
