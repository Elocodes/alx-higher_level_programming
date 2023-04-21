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


class Rectangle(Base):
    """This class inherits from the base.

    its function calls the init of the base class to get the id attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """function initializes the size of the rectangle.

        Args:
            width, height, x and y may be any value
            width and height must be given
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """function gets the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """function sets the value of the private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """function gets the private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """function sets the value of the private attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """function gets the private attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """function sets the value of the private attribute height"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """function returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """function prints the shape of the rectangle using the symbol '#'

        if the args x and y are passed, the shape is pushed to the right by
        x times and down by y times
        """
        rect = ''

        if self.__x and self.__y:
            print('\n' * self.__y, end='')
            for i in range(self.__height):
                rect += (' ' * self.__x) + ('#' * self.__width) + '\n'
            print(rect, end='')

        elif self.__x:
            for i in range(self.__height):
                rect += (' ' * self.__x) + ('#' * self.__width) + '\n'
            print(rect, end='')

        elif self.__y:
            print('\n' * self.__y, end='')
            print('\n'.join('#' * self.__width for row
                            in range(self.__height)))
        else:
            print('\n'.join('#' * self.__width for row
                            in range(self.__height)))

    def __str__(self):
        """function returns a rectangle with its attributes in the form

        rectangle id x/y w/h
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """function assigns an argument to each attribute.

        The attributes receive arguments according to the specified order.
        the arguments can be updated from one value to another
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
