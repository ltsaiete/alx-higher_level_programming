#!/usr/bin/python3
"""
This is the module 3-say_my_name
It only contains one function called say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>

    Args:
        first_name (string): First name
        last_name (string): last name

    Returns:
        void
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')

    if type(last_name) != str:
        raise TypeError('last_name must be a string')

    if last_name != "":
        last_name = " " + last_name

    print(f'My name is {first_name}{last_name}')
