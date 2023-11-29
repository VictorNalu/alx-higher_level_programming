#!/usr/bin/python3
def uppercase(str):
    for i in str:
        stringg = i
        if ord(stringg) >= 97 and ord(stringg) <= 122:
            stringg = chr(ord(i) - 32)      
        print("{}".format(stringg), )
