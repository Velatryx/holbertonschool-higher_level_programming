#!/usr/bin/python3
"""Defines a function that returns Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal triag"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        new_row = [1]

        for j in range(len(prev) - 1):
            new_row.append(prev[j] + prev[j + 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
