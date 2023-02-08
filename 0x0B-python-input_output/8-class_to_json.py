#!/usr/bin/python3
"""
This is a simple module and it only has
one function called class_to_json
"""


def class_to_json(obj):
    """
    This function returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:

    Args:
        obj(object): the object

    Returns:
        the dictionary description
    """
    return obj.__dict__
