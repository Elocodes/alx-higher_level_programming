#!/usr/bin/python3
"""
This module tests the Rectanglee class that inherits from the Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class test_Rectangle_inputs(unittest.TestCase):
    """Class tests rectangle data to ensure id attributes is set and
    
    updates accordingly with the private class attribute
    """
    def test_id_none(self):
        """function tests that inherited init works.other values
        of the rectangle can be of any value

        Does Rectangle id increment when id value is not given?
        """
        call1 = Rectangle(2, 1, 4, 4, id=None)
        call2 = Rectangle(2, 1, 0, 2, id=None)
        self.assertEqual(call1.id, call2.id - 1)

    def test_id_given(self):
        """function tests that inherited init works.other values
        of the rectangle can be of any value

        Does Rectangle id print passed value if given?
        """
        call1 = Rectangle(2, 1, 4, 3, 0)
        call2 = Rectangle(2, 1, 0, 4, -4)
        call3 = Rectangle(2, 1, 4, 3, 5)
        self.assertEqual(call1.id, 0)
        self.assertEqual(call2.id, -4)
        self.assertEqual(call3.id, 5)

    def test_integer_inputs(self):
        """function tests that inputs of width, height, x and y are integers.

        Does the input of a non integer type for the args raise an exception?
        """
        self.assertRaises(TypeError, lambda: Rectangle('hi', 2, 4, 3), msg='width must be an integer')
        self.assertRaises(TypeError, lambda: Rectangle(2, [6], 4, 3), msg='height must be an integer')
        self.assertRaises(TypeError, lambda: Rectangle(2, 2, {}, 3), msg='x must be an integer')
        self.assertRaises(TypeError, lambda: Rectangle(2, 2, 4, 3.2), msg='y must be an integer')

    def test_values_positive(self):
        """function tests that args are positive.

        width and height must be greater than 0
        x and y must be greater than or equal to 0
        """
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-6, 2, 4, 3)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(2, 0, 4, 3)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(2, 2, -1, 3)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(2, 2, 4, -100)
