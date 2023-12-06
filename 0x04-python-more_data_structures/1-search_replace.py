#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == [] or my_list is None:
        return []
    new_list = [replace if elmnt is search else elmnt for elmnt in my_list]
    return new_list
