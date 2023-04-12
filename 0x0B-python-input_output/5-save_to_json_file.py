#!/usr/bin/python3

import json

"""
This module contains function that writes to a text file
"""


def save_to_json_file(my_obj, filename):
    """function writes to a text file using a JSON representation.
    function creates the file if not existing and overwrites its
    its contents if it does. The with statement is used to open and
    read the file. Exceptions are not managed."""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
