#!/usr/bin/python3
"""Return the list of available attributes and methods of an object."""


def lookup(obj):
    """Return a sorted list of attributes and methods available on obj."""
    return sorted(dir(obj))
