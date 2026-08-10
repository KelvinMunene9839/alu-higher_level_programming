#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
import sys
import models.rectangle
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for Rectangle instantiation."""

    def test_is_base_instance(self):
        """A Rectangle should also be an instance of Base."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_width_height(self):
        """width and height should be set from the constructor."""
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)

    def test_default_x_y(self):
        """x and y should default to 0."""
        r = Rectangle(3, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_given_x_y(self):
        """x and y should be set from the constructor."""
        r = Rectangle(3, 5, 1, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_given_id(self):
        """A given id should be used instead of an auto-incremented one."""
        r = Rectangle(3, 5, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_auto_id(self):
        """Two instances without an id get sequential ids."""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, r1.id + 1)


class TestRectangleValidation(unittest.TestCase):
    """Tests for Rectangle attribute validation."""

    def test_width_not_int(self):
        """A non-int width should raise a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 10)

    def test_height_not_int(self):
        """A non-int height should raise a TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_x_not_int(self):
        """A non-int x should raise a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_y_not_int(self):
        """A non-int y should raise a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, [])

    def test_width_zero(self):
        """A width of 0 should raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        """A negative width should raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_zero(self):
        """A height of 0 should raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        """A negative height should raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_negative(self):
        """A negative x should raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_y_negative(self):
        """A negative y should raise a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_x_zero_is_valid(self):
        """An x of 0 should be valid."""
        r = Rectangle(10, 2, 0)
        self.assertEqual(r.x, 0)

    def test_width_bool_rejected(self):
        """A boolean width should be rejected as not an integer."""
        with self.assertRaises(TypeError):
            Rectangle(True, 2)

    def test_width_float_rejected(self):
        """A float width should be rejected as not an integer."""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_setter_validation(self):
        """Setters should apply the same validation as the constructor."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area."""

    def test_area(self):
        """area should return width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for Rectangle.display."""

    def capture_display(self, rect):
        """Return the captured stdout of rect.display()."""
        captured = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured
        try:
            rect.display()
        finally:
            sys.stdout = old_stdout
        return captured.getvalue()

    def test_display_no_offset(self):
        """display() should print a width x height block of '#'."""
        output = self.capture_display(Rectangle(2, 2))
        self.assertEqual(output, "##\n##\n")

    def test_display_with_offset(self):
        """display() should offset the block by x and y."""
        output = self.capture_display(Rectangle(2, 3, 2, 2))
        self.assertEqual(output, "\n\n  ##\n  ##\n  ##\n")


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__."""

    def test_str(self):
        """__str__ formats as [Rectangle] (id) x/y - width/height."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for Rectangle.update with no-keyword arguments."""

    def test_update_id(self):
        """The first argument should update id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_all(self):
        """All five arguments should update in the documented order."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        actual = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(actual, (89, 2, 3, 4, 5))

    def test_update_partial(self):
        """Fewer arguments should only update the leading attributes."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        actual = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(actual, (89, 2, 10, 10, 10))

    def test_update_no_args(self):
        """No arguments should leave every attribute unchanged."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        actual = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(actual, (1, 10, 10, 10, 10))


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for Rectangle.update with keyworded arguments."""

    def test_update_kwargs(self):
        """Keyword arguments should update the matching attributes."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_kwargs_multiple(self):
        """Multiple keyword arguments should all be applied."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        actual = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(actual, (89, 2, 10, 3, 1))

    def test_args_take_priority_over_kwargs(self):
        """kwargs should be skipped when args is not empty."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(2, id=99)
        self.assertEqual(r.id, 2)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def test_keys(self):
        """The dictionary should contain id, width, height, x and y."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(
            d, {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_return_type(self):
        """to_dictionary should return a dict."""
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_round_trip(self):
        """A Rectangle rebuilt from its dictionary should be equal."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


class TestRectangleDocstrings(unittest.TestCase):
    """Tests documentation of the Rectangle module, class and methods."""

    def test_module_doc(self):
        """The module should be documented."""
        self.assertIsNotNone(models.rectangle.__doc__)

    def test_class_doc(self):
        """The class should be documented."""
        self.assertIsNotNone(Rectangle.__doc__)

    def test_method_docs(self):
        """Every method should be documented."""
        methods = [
            Rectangle.__init__, Rectangle.area, Rectangle.display,
            Rectangle.__str__, Rectangle.update, Rectangle.to_dictionary,
        ]
        for method in methods:
            self.assertIsNotNone(method.__doc__)


if __name__ == "__main__":
    unittest.main()
