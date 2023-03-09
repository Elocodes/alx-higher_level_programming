#!/usr/bin/python3

"""def uppercase(str):
    function prints a string in uppercase
    for each_letter in str:
        each_letter = ord(each_letter)
        if each_letter in range(97, 123):
            each_letter -= 32
        to_upper = chr(each_letter)
        print("{}".format(to_upper), end='')
    print("")"""

#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if i >= 97 and i <= 122:
            i -= 32
        i = chr(i)
        print("{}".format(i), end='')
    print("")
