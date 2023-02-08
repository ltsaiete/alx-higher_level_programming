#!/usr/bin/python3
"""
This is a simple module and it only has
one function called from_json_string(my_str)
"""


def from_json_string(my_str):
    """
    This function returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str(str): json string

    Returns:
        an object
    """
    import json
    return json.loads(my_str)
