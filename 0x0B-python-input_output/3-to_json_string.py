#!/usr/bin/python3

import json

"""
module contains function that returns JSON string
"""


def to_json_string(my_obj):
    """function returns the JSON representation of an object"""
    return json.dumps(my_obj)
