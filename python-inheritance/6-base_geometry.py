#!/usr/bin/python3
"""A basic geometry module with area support."""


class BaseGeometry:
    """Base class for geometry-related operations."""

    def area(self):
        """Raise an exception because the area is not implemented."""
        raise Exception("area() is not implemented")
