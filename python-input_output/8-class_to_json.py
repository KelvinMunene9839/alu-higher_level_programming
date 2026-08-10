#!/usr/bin/python3
"""Module that converts a simple object instance to a JSON-serializable
dictionary."""


def class_to_json(obj):
    """Return the dictionary description of a simple object instance."""
    return obj.__dict__
