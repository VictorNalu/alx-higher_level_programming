#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == [] or my_list is None:
        return []
    new_list = [replace if element is search else element for element in my_list]
    return new_list
