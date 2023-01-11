#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None

    newList = []
    for i, item in enumerate(my_list):
        newList.append(item)
        if item == search:
            newList[i] = replace

    return newList
