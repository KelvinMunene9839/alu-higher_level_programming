#!/usr/bin/python3
"""Defines a function that adds two integers or floats."""


def add_integer(a, b=98):
    """Add a and b together and return the result as an integer.

    Both a and b are cast to int before being added. Either
    argument may be an int or a float; any other type raises
    a TypeError.

    Args:
        a: the first number, an integer or a float.
        b: the second number, an integer or a float. Defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
