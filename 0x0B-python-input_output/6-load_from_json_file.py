#!/usr/bin/python3

"""
This module contains function that creates an object from a Json file
"""

import json


def load_from_json_file(filename):
    """function writes to a text file using a JSON representation.

    function creates the file if not existing and overwrites its
    its contents if it does. The with statement is used to open and
    read the file. Exceptions are not managed.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
