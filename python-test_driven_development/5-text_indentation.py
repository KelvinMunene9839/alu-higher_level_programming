#!/usr/bin/python3
"""Defines a function that prints text with extra indentation."""


def text_indentation(text):
    """Print text, adding two new lines after each '.', '?' and ':'.

    Leading and trailing spaces are removed from each printed line.

    Args:
        text: the string to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        if char == " " and (line == "" or line[-1] in ".?:\n"):
            continue
        line += char
        if char in ".?:":
            print(line)
            print()
            line = ""
    if line:
        print(line)
