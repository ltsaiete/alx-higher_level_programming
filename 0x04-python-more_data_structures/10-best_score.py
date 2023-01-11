#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    bigKey, bigValue = list(a_dictionary)[
        0], a_dictionary[list(a_dictionary)[0]]

    for k, v in a_dictionary.items():
        if v > bigValue:
            bigValue = v
            bigKey = k

    return bigKey
