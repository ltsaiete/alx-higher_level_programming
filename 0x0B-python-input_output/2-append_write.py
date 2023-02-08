#!/usr/bin/python3
"""
This is a simple module and it only has
one function called append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    Write a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:

    Args:
        filename(str): name of the file
        text(str): text to append

    Returns:
        number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f:
        chars = f.write(text)
        return chars
