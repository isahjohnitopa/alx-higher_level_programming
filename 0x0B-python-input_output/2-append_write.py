#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file.

    Argr:
        filename (str): The file to be appended
        text (str): The string to be appended
    Returns:
        Return the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
