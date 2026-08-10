#!/usr/bin/python3
"""Module that defines a Student class with a filterable JSON export."""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with a first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only the attributes whose names
        are listed are included; otherwise all attributes are included.
        """
        if isinstance(attrs, list) and all(
                isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
