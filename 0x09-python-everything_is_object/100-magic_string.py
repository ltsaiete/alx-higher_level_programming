#!/usr/bin/python3
def magic_string():
    magic_string.c = hasattr(magic_string, 'c') and magic_string.c+1 or 1
    return ", ".join(["BestSchool"] * magic_string.c)
