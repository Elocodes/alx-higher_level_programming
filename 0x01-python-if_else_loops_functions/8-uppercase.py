#!/usr/bin/python3

def uppercase(str):
    """function prints a string in uppercase"""
    for each_letter in str:
        each_letter = ord(each_letter)
        if each_letter in range(97, 123):
            each_letter -= 32
        to_upper = chr(each_letter)
        print("{}".format(to_upper), end='')
    print()
