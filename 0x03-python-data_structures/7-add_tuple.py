#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = []
    for i in range(2):
        new = 0
        if len(tuple_a) > i:
            new += tuple_a[i]
        if len(tuple_b) > i:
            new += tuple_b[i]
        sum_tuple.append(new)

    return (sum_tuple[0], sum_tuple[1])
