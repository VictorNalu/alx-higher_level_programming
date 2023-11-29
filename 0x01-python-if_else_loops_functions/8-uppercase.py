#!/usr/bin/python3
def uppercase(str):
    for strin in str:
        value = strin
        if ord(value) >= 97 and ord(value) <= 122:
            value = chr(ord(strin) - ord('a') + ord('A'))
        print("{}".format(value),)
     
