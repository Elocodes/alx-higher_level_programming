#!/usr/bin/python3

"""
module contains function that returns JSON string
"""

import json


def to_json_string(my_obj):
    """function returns the JSON representation of an object.

    Args:
        param: my_obj is of type that is JSON serializable
    """
    return json.dumps(my_obj)
