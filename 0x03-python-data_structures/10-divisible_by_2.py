#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for elem in my_list:
        if elem % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
