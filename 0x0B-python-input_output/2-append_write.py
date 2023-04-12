#!/usr/bin/python3

"""
This module contains function that writes and appends to a text file
"""


def append_write(filename="", text=""):
    """function writes to a text file and returns the number of characters
    written. function creates the file if not existing and overwrites its
    its contents if it does..
    The with statement is used to open and read the file. Exceptions are
    not managed."""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
