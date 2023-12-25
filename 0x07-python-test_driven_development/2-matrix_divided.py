#!/usr/bin/python3
""" This is "2-matrix_divided.py" module.
This module supplies one function, matrix_divided. For example,
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Returns matrix of quotients of matrix and div
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """

    is_matrix = True
    for element in matrix:
        if not isinstance(element, list):
            is_matrix = False
            break
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not is_matrix:
        raise TypeError(msg)

    contains_nums = True
    for element in matrix:
        for i in element:
            if not isinstance(i, (int, float)):
                contains_nums = False
                break
    if not contains_nums:
        raise TypeError(msg)

    len_element = len(matrix[0])
    is_same_size = True
    for i in range(1, len(matrix)):
        if len_element != len(matrix[i]):
            is_same_size = False
            break
        len_element = len(matrix[i])

    if not is_same_size:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for element in matrix:
        quotient = [round(i / div, 2) for i in element]
        new_matrix.append(quotient)
    return new_matrix
