#!/usr/bin/python3

# function prints the number and words of arguments passed
# to the command line. the num and enumarate funct helps
# provide the numbered list starting from 1

import sys

if __name__ == "__main__":

    count = len(sys.argv)
    # arg = []
    arg = sys.argv[1:]

    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("{} " "argument:".format(count - 1))
        for num, i in enumerate(arg, 1):
            print(f"{num}: {i}")
    else:
        print("{} " "arguments:".format(count - 1))
        for num, i in enumerate(arg, 1):
            print(f"{num}: {i}")
