#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    bigKey, bigValue = None, float('-inf')

    for k, v in a_dictionary.items():
        if v > bigValue:
            bigValue = v
            bigKey = k

    return bigKey
