#!/usr/bin/python3
def no_c(my_string):
    ls = list(my_string)
    for i, c in enumerate(ls):
        if c == "c" or c == "C":
            ls[i] = ""
    my_string = ''.join(ls)
    return my_string
