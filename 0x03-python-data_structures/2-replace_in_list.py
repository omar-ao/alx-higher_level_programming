#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    llen = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= llen:
        return my_list
    my_list[idx] = element
