#!/usr/bin/python3
"""Defines a function that divides every element of a matrix."""


def matrix_divided(matrix, div):
    """Divide every element of matrix by div and return a new matrix.

    Args:
        matrix: a list of lists of integers or floats, where every
            row has the same length.
        div: the integer or float divisor.

    Returns:
        A new matrix with every element divided by div and rounded
        to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of integers or
            floats, if the rows of matrix don't all have the same
            size, or if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    matrix_error = "matrix must be a matrix (list of lists) of " \
        "integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(matrix_error)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(matrix_error)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(matrix_error)
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
