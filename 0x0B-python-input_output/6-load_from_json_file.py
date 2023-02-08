#!/usr/bin/python3
"""
This is a simple module and it only has
one function called load_from_json_file(filename)
"""


def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”:

    Args:
        filename(str): the filename

    Returns:
        an object
    """
    import json
    with open(filename) as f:
        return json.load(f)
