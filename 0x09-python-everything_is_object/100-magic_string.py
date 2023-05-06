#!/usr/bin/python3
def magic_string():
    if not hasattr(magic_string, "count"):
        magic_string.count = 0
    magic_string.count += 1
    return ", ".join(["BestSchool"] * magic_string.count)
