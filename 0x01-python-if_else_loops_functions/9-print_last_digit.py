#!/usr/bin/python3

def print_last_digit(number):
    """function prints the last digit of a number"""
    cast = str(number)
    last_digit = cast[-1]
    digit2int = int(last_digit)
    print("{}".format(digit2int), end='')
    return (digit2int)
