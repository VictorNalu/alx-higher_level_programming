#!/usr/bin/python3
"""A module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each line,
    containing a specific string.

    parameters:
        filename (str, optional): name of file. Defaults to "".
        search_string (str, optional): string to search. Defaults to "".
        new_string (str, optional): string to append. Defaults to "".
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fi:
        txt = ""
        for line in text:
            txt += line
            if search_string in line:
                txt += new_string
        fi.write(txt)
