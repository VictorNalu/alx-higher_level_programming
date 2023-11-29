#!/usr/bin/python3
def uppercase(str):
    for iterator in str:
        stringg = iterator
        if ord(stringg) >= 97 and ord(stringg) <= 122:
            stringg = chr(ord(iterator) - 32)
        print("{}".format(stringg), )
