#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Max of an ascending list is its last element."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of an unordered list is found correctly."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Max of a descending list is its first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Max of a single-element list is that element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Max of an empty list is None."""
        self.assertIsNone(max_integer([]))

    def test_default_empty_list(self):
        """Calling with no argument uses the default empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Max works correctly with negative numbers."""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_sign_numbers(self):
        """Max works correctly with a mix of positive and negative."""
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

    def test_duplicate_max(self):
        """Max is returned even if it appears more than once."""
        self.assertEqual(max_integer([4, 1, 4, 2]), 4)

    def test_floats(self):
        """Max works correctly with floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
