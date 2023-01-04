#!/usr/bin/python3
def islower(c):
    ascii = ord(c)
    if ascii >= 97 and ascii <= 122:
        return True
    return False
