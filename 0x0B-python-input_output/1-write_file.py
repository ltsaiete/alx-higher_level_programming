#!/usr/bin/python3
"""
This is a simple module and it only has
one function called write_file(filename="", text=""):
"""


def write_file(filename="", text=""):
    """
    This function reads a text file (UTF8) and prints it to stdout

    Args:
        filename(str): name of the file
        text(str): text to write

    Returns:
        the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        chars = f.write(text)
        return chars
