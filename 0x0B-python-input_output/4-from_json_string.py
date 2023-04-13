#!/usr/bin/python3

"""
module contains function that returns an object represented
by a JSON string
"""

import json


def from_json_string(my_str):
    """function returns the deserialized version of an object
    represented by a JSON string.

    Arg:
        my_str

    Raises exception if file cannot be encoded
    """
    return json.loads(my_str)
