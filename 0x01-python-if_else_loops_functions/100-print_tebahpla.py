#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        ch = chr(i)
        print(ch, end='')
    else:
        ch = chr(i-32)
        print(ch, end='')
