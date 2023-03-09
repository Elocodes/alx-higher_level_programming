#!/usr/bin/python3

def fizzbuzz():
    """function prints numbers from 1 to 100 replacing multiples of 3 and 5
    with fizz and buzz respectively.
    if number is a multiple of both 3 and 5, replace with fizzbuzz"""
    for each_num in range(1, 101):
        if each_num % 3 == 0 and each_num % 5 == 0:
            print("FizzBuzz ", end='')
        elif each_num % 3 == 0:
            print("Fizz ", end='')
        elif each_num % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(each_num), end='')
