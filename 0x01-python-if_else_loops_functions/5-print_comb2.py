#!/usr/bin/python3

# 02d - formats an integer(d) to a minimum width of 2
# so if a single digit, it adds a padding of 0 to the left

for each_num in range(0, 100):
    if each_num == 99:
        print("99")
    else:
        print("{:02d}, ".format(each_num), end='')
