#!/usr/bin/python3

space = " "

for each_num in range(0, 100):
    if each_num == 99:
        print("99")
    else:
        if each_num < 10:
            num2str = str(each_num)
            str_zero = '0'
            to_print = str_zero + num2str
        else:
            to_print = each_num
        print("{}, {}".format(to_print, space), end='')
