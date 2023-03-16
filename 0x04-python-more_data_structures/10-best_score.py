#!/usr/bin/python3

def best_score(a_dictionary):
    """function returns a key with the biggest integer value"""

    if a_dictionary is None:
        return None
    else:
        max_val = max(a_dictionary)
        return max_val
