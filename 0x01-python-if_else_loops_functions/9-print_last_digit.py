#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
       last_dit = (-number % 10)
    elif number >= 0:
         last_dit = number % 10
    print("{}".format(last_dit), end="")
    return last_dit
