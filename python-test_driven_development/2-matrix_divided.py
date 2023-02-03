#!/usr/bin/python3
"""this function devide a matrix"""


def matrix_divided(matrix, div):
    """this is the function that devide the matrix"""
    if not isinstance(matrix, list):
        for i in range(len(matrix)):
            if not isinstance(matrix[i], list):
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int):
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(matrix) < 2:
            continue
        for j in matrix:
            if len(i) != len(j):
                raise TypeError(
                  "Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    for row in matrix:
        new.append(row[:])
    for i in range(len(new)):
        for j in range(len(new[i])):
            new[i][j] = round((new[i][j] / div), 2)
    return new
