#!/usr/bin/python3
"""
This is a simple module and it only has
one function called save_to_json_file(my_obj, filename)
"""


def save_to_json_file(my_obj, filename):
    """
    This function  writes an Object to a text file,
    using a JSON representation:

    Args:
        my_obj(object): The object to write
        filename(str): The file name

    Returns:
        void
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
