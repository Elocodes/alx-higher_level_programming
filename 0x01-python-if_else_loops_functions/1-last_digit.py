#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number > 0):
    lastdigit = number % 10
    if (lastdigit == 0):
        print(f"Last digit of {number} is {lastdigit} and is 0")
    elif (6 > lastdigit > 0):
        print(f"Last digit of {number} is {lastdigit} and \
is less than 6 and not 0")
    elif(lastdigit >= 6):
        print(f"Last digit of {number} is {lastdigit} and is greater than 5")

elif(number < 0):
    num2str = str(number)
    last2int = int(num2str[len(num2str) - 1])
    if (last2int != 0):
        print(f"Last digit of {number} is {-last2int} and \
is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last2int} and is 0")
