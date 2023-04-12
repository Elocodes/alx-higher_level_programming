#!/usr/bin/python3

"""
This module contains function tha reads a text file
"""


def read_file(filename=""):
    """function reads a text file and prints it to stdout.
    The with statement is used to open and read the file. Exceptions are
    not managed."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
