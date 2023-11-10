#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight = 0
    count = 0
    for elem in my_list:
        a, b = elem
        weight += a * b
        count += b
    return weight / count
