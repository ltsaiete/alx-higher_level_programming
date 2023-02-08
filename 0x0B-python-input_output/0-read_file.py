#!/usr/bin/python3
"""
This is a simple module and it only has
one function called read_file(filename="")
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout

    Args:
        filename(str): name of the text file

    Returns:
        void
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read())
