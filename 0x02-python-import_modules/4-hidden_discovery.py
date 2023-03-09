#!/usr/bin/python3

# function imports a compiled module and
# prints only its attributes not preceeded by a "__"

import hidden_4

if __name__ == "__main__":
    hid_list = dir(hidden_4)
    crop_list = []

    for each_item in hid_list:
        if each_item[0:2] != "__":
            crop_list.append(each_item)
    for items in crop_list:
        print(items)
