#!/usr/bin/python3

"""
This module contains function that writes to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """function writes to a text file using a JSON representation.

    function creates the file if not existing and overwrites its
    its contents if it does.

    Args:
        my_obj
        filename

    Raises Exception if file cannot be encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
