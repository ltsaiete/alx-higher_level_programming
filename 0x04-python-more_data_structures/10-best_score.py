#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    bigKey, bigValue = None, a_dictionary[list(a_dictionary)[0]]

    for k, v in a_dictionary.items():
        if v > bigValue and v != None:
            bigValue = v
            bigKey = k

    return bigKey
