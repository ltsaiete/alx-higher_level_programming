#!/usr/bin/python3
"""
This is a simple module and it only has
one class called LockedClass
"""


class LockedClass():
    """
    class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    """

    __slots__ = ['first_name']

    def __init__(self):
        pass
