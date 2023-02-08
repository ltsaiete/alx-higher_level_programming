#!/usr/bin/python3
"""
This is a simple module and it only has
one function called to_json_string(my_obj)
"""


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        my_obj(object): The object we are reading

    Returns:
        JSON representation of an object
    """
    import json

    return json.dumps(my_obj)
