#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    score, weight = 0, 0

    for item in my_list:
        a, b = item
        score += a * b
        weight += b
    return score / weight
