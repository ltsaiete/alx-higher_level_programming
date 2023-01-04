#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        ch = chr(i)
    else:
        ch = chr(i-32)

    print('{:c}'.format(ch), end='')
