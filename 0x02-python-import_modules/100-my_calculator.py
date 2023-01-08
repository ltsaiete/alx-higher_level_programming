#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, div, mul, sub
    args = sys.argv
    if len(args) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a, op, b = int(args[1]), args[2], int(args[3])
        res = 0

        if op == '+':
            res = add(a, b)
        elif op == '-':
            res = sub(a, b)
        elif op == '*':
            res = mul(a, b)
        elif op == '/':
            res = div(a, b)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)

        print(f'{a} {op} {b} = {res}')
