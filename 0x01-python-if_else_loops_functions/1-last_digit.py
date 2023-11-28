#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = (number) % 10
if number < 0:
    lastd = -(lastdigit)
x = "Last digit of {} is {}" .format(number, lastdigit)
if lastdigit > 5:
    print(f"{x} and is greater than 5")
elif lastdigit == 0:
    print(f"{x} and is 0")
elif lastdigit < 6:
    print(f"{x} and is less than 6 and not 0")
