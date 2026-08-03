#!/usr/bin/python3
"""Square implementation with custom string representation."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with validated size."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
