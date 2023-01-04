#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii = ord(c)
        if ascii >= 97 and ascii <= 122:
            ascii -= 32
        print('{:c}'.format(ascii), end='')

    print()
