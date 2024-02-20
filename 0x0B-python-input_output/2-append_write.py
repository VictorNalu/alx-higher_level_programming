#!/usr/bin/python3
"""A module that contains the function, append_write"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number
    of characters added.

    parameter:
        filename (str, optional): name of the file. Defaults as "".
        text (str, optional): string of text to write to file. Default as "".

    Returns:
        int: number of characters appended to file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        """This method returns the number of characters added to a file."""
        return f.write(text)
