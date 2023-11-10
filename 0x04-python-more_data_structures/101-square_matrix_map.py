#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squares = []
    for elem in matrix:
        squares.append(list(map(lambda n: n * n, elem)))
    return squares
