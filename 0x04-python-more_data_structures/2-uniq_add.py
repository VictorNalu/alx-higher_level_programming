#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for element in set(my_list):
        add += int(element)
    return add
