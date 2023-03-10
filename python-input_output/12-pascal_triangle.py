#!/usr/bin/python3
"""This is the declaration of the module"""


def pascal_triangle(n):
    """this function create apascal triangle"""
    result = []
    if n <= 0:
        return result
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            row = [1]
            for j in range(i-1):
                row.append(result[i-1][j] + result[i-1][j+1])
            row.append(1)
            result.append(row)
    return result
