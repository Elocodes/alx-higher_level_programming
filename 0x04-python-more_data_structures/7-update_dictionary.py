#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """function updates value if key already exists or adds new key/value pair
    in dict if not"""

    a_dictionary[key] = value
    return (a_dictionary)
