#!/usr/bin/python3
"""This module conatins the base class.

his class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all future classes and to avoid
duplicating the same code (by extension, same bugs)
"""


class Base():
    """class sets the id attribute.

    it contains one private class attribute, and the init function.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
