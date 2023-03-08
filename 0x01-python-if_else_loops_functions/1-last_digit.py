#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = str(number)[-1]
digit2int = int(last_digit)
neg_last_digit = -1 * digit2int

if digit2int > 5:
    if number > 0:
        print(f"Last digit of {number:d} is {digit2int:d} and \
                is greater than 5")
    elif number < 0:
        print(f"Last digit of {number:d} is {neg_last_digit:d} and \
                is less than 6 and not 0")
elif digit2int in range(1, 6):
    if number > 0:
        print(f"Last digit of {number:d} is {digit2int:d} and \
                is less than 6 and not 0")
    elif number < 0:
        print(f"Last digit of {number:d} is {neg_last_digit:d} and \
                is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {digit2int} and is 0")
