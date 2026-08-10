#!/usr/bin/python3
"""Defines a function that prints a square made of the # character."""


def print_square(size):
    """Print a size by size square using the '#' character.

    Args:
        size: the length of a side of the square. Must be a
            non-negative integer.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is an integer smaller than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
