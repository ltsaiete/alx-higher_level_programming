#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a, op, b = int(args[1]), args[2], int(args[3])
        res = 0

        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '/':
            res = a / b
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)

        print(f'{a} {op} {b} = {res}')
