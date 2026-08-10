#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
import models.square
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for Square instantiation."""

    def test_is_rectangle_instance(self):
        """A Square should also be an instance of Rectangle."""
        self.assertIsInstance(Square(5), Rectangle)

    def test_width_height_equal_size(self):
        """width and height should both equal size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """x and y should default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_given_x_y(self):
        """x and y should be set from the constructor."""
        s = Square(3, 1, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_given_id(self):
        """A given id should be used instead of an auto-incremented one."""
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_size_validation(self):
        """size validation should follow Rectangle's width validation."""
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(ValueError):
            Square(-5)


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__."""

    def test_str(self):
        """__str__ formats as [Square] (id) x/y - size."""
        s = Square(5, 1, 3, 3)
        self.assertEqual(str(s), "[Square] (3) 1/3 - 5")


class TestSquareSize(unittest.TestCase):
    """Tests for the Square.size property."""

    def test_getter(self):
        """size should return the current width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_setter(self):
        """Setting size should update both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_setter_validation(self):
        """size should use the same validation as width."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for Square.update with no-keyword arguments."""

    def test_update_all(self):
        """All four arguments should update in the documented order."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    def test_update_partial(self):
        """Fewer arguments should only update the leading attributes."""
        s = Square(5, 0, 0, 1)
        s.update(1, 2)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 0, 0))


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for Square.update with keyworded arguments."""

    def test_update_kwargs(self):
        """Keyword arguments should update the matching attributes."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 7, 0, 1))

    def test_args_take_priority_over_kwargs(self):
        """kwargs should be skipped when args is not empty."""
        s = Square(5, 0, 0, 1)
        s.update(2, size=99)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 5)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def test_keys(self):
        """The dictionary should contain id, size, x and y."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_round_trip(self):
        """A Square rebuilt from its dictionary should be equal."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


class TestSquareDocstrings(unittest.TestCase):
    """Tests documentation of the Square module, class and methods."""

    def test_module_doc(self):
        """The module should be documented."""
        self.assertIsNotNone(models.square.__doc__)

    def test_class_doc(self):
        """The class should be documented."""
        self.assertIsNotNone(Square.__doc__)

    def test_method_docs(self):
        """Every method should be documented."""
        methods = [
            Square.__init__, Square.__str__, Square.update,
            Square.to_dictionary,
        ]
        for method in methods:
            self.assertIsNotNone(method.__doc__)


if __name__ == "__main__":
    unittest.main()
