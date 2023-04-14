#!/usr/bin/python3
"""This module contains script that adds and loads argument outputs
to a list. TH elist will be saved as a JSON representation"""


import json
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

my_list = load_from_json_file(filename)
save_to_json_file([], filename)

if len(sys.argv) > 1:
    my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
