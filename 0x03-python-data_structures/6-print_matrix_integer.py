#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for n in element:
            print("{:d}".format(n), end="")
            if element[len(element) - 1] != n:
                print(" ", end="")
        print()
