#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv)
    if count == 1:
        print('0 arguments.')
    elif count == 2:
        print('1 argument:')
    else:
        print(f'{count - 1} arguments:')

    for i in range(1, count):
        print(f'{i}: {sys.argv[i]}')
