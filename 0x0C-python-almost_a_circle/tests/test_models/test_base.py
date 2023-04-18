#!/usr/bin/python3
"""
This module tests the base class to see if the id attribute is set.
"""
import unittest
from models.base import Base

class testBaseid(unittest.TestCase):
    """Class tests base data to ensure id attributes is set and
    
    updates accordingly with the private class attribute
    """
    def test_idvalue_none(self):
        """function tests that id is incremented when no value is passed for it.

        Does Base() work?
        """
        call_1 = Base()
        call_2 = Base()
        self.assertEqual(call_1.id, call_2.id - 1)

    def test_idvalue_given(self):
        """function tests that id is returned with the value passed

        Does Base(3) work?
        """
        call = Base(3)
        call2 = Base(-5)
        call3 = Base(0)
        self.assertEqual(call.id, 3)
        self.assertEqual(call2.id, -5)
        self.assertEqual(call3.id, 0)
