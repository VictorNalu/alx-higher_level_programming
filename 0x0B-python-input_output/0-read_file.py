#!/usr/bin/python3
"""Module containing the function read_file"""


def read_file(filename=""):
    """Reads a file and prints to stdout.

    parameter:
        filename (str, optional): name of file to read. ("") as default.
    """
    with open(filename, "r", encoding="utf-8") as f:
        file_read = f.read()
        print(file_read, end="")
