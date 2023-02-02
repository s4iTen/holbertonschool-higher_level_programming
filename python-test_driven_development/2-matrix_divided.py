#!/usr/bin/python3
"""this function devide a matrix"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list) and isinstance([i for i in matrix[i]], list):
        if not isinstance([j for i in matrix[i][j]], int):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len([i for i in range(len(matrix))]) > len([i + 1 for i in range(len(matrix))]):
        raise TypeError("Each row of the matrix must have the same size")
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
