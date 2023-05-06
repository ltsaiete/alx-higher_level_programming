#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'count', hasattr(magic_string, 'count') and getattr(magic_string, 'count')+1 or 0)
    return ", ".join(["BestSchool"] * magic_string.count)
