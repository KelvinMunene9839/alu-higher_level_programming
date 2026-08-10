#!/usr/bin/python3
"""Module that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's
    triangle of n rows. Returns an empty list if n <= 0."""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(len(prev) - 1):
            row.append(prev[j] + prev[j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
