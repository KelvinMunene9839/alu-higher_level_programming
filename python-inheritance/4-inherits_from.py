#!/usr/bin/python3
"""Check whether an object inherits from a class but is not the class itself."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class indirectly or directly."""
    return isinstance(obj, a_class) and type(obj) is not a_class
