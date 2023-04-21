#!/usr/bin/python3
"""This module contains the class quare and its methods.

The square class inherits from the rectangle class, and the
rectangle class inherits from the base
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class inherits from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """function initializes the attributes of square.

        since square is a special rectangle, it will inherit the attributes
        of rectangle. we call the init of rectangle to instantiate this
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """function assigns value to size of the square
        width == height == size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """function retrun the attributes of the shape.

        calls rectangle __str__ function
        """
        return("[{}] ({}) {}/{} - {}".format(__class__.__name__,
               self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """function assigns arguments to attributes.

        calls the rectangle update function
        """
        if args is None or len(args) == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    self.__setattr__(key, value)
                return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """function returnst the dict represntation of the
        square attributes"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
