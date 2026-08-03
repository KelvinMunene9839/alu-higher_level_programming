#!/usr/bin/python3
"""A list subclass with a sorted-printing method."""


class MyList(list):
    """List subclass that can print its contents in sorted order."""

    def print_sorted(self):
        """Print the list elements in ascending order."""
        print(sorted(self))
