#!/usr/bin/python3

import json

"""
module contains function that returns an object represented
by a JSON string
"""


def from_json_string(my_str):
    """function returns the deserialized version of an object
    represented by a JSON string"""
    return json.loads(my_str)
