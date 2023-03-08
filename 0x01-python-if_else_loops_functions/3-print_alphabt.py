#!/usr/bin/python3

alphabt = ""
i = 122
j = 97
while (j <= i):
    alphabt += chr(j)
    j += 1
    if (j == 101):
        j += 1
    if (j == 113):
        j += 1
print("{}".format(alphabt), end="")
