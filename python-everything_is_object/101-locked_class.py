#!/usr/bin/python3
"""Locked class that only allows the first_name attribute."""


class LockedClass:
    """Prevent dynamic creation of instance attributes except first_name."""

    __slots__ = ["first_name"]
