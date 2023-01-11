#!/usr/bin/python3
def best_score(a_dictionary):
    bigKey, bigValue = list(a_dictionary)[
        0], a_dictionary[list(a_dictionary)[0]]

    for k, v in a_dictionary.items():
        if v > bigValue:
            bigValue = v
            bigKey = k

    return bigKey
