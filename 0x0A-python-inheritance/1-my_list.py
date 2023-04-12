#!/usr/bin/python3

"""This module demonstrates inheritance in python..

The subclass: MyList
The parentclass: list
"""


class MyList(list):
    """class inherits from the parentclass list.

    Arg:
        param: list is an inbuilt python class. other classes can
        inherit from it.
        """
    def __init__(self):
        """function initializes attributes.

        Here, the init method of the parentclass will be called.
        This will allow our subclass use its attributes.
        """
        list.__init__([])

    def print_sorted(self):
        """function prints the contents of a list in ascending order.
        in this case, all elements of list are of type int.
        """
        print(sorted(self))
