#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy = my_list.copy()
    for i, v in enumerate(my_list):
        if search == v:
            cpy[i] = replace
    return cpy
