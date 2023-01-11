#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = list(set(my_list))
    sum = 0
    for item in uniques:
        sum += item

    return sum
