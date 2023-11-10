#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda elem: list(map(lambda n: n * n, elem)), matrix))
