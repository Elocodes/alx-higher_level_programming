#!/usr/bin/python3

# function adds the arguments passed to the command line.
# since args are usually str, each on is cast into an int
# first before the addition.

import sys

if __name__ == "__main__":

    addition = 0
    arg = sys.argv[1:]
    for i in arg:
        str2int = int(i)
        addition += str2int
    print(addition)
