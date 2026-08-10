#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base instantiation."""

    def test_id_is_public(self):
        """id should be set as a public attribute."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_given_id(self):
        """A given id should be used as-is, even if not sequential."""
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_negative_id(self):
        """A negative id should be accepted as given."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_auto_id_increments(self):
        """Two instances without an id get sequential ids."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_no_args_no_kwargs(self):
        """Base() should not raise."""
        Base()

    def test_docstrings(self):
        """Base, its module and its methods should be documented."""
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)


class TestBaseToJSONString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none(self):
        """None should return "[]"."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list should return "[]"."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """A list of dicts should be converted to valid JSON."""
        list_dicts = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(result), list_dicts)

    def test_return_type(self):
        """The return value should be a string."""
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)


class TestBaseFromJSONString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none(self):
        """None should return an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string should return an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        """A valid JSON string should return the matching list."""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = json.dumps(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_return_type(self):
        """The return value should be a list."""
        self.assertIsInstance(
            Base.from_json_string(json.dumps([{"id": 1}])), list)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_creates_file(self):
        """save_to_file should create a file named <Class>.json."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_file_content(self):
        """The file should hold the JSON representation of the list."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as jsonfile:
            content = jsonfile.read()
        self.assertEqual(json.loads(content), [r1.to_dictionary()])

    def test_none_saves_empty_list(self):
        """Passing None should save an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as jsonfile:
            content = jsonfile.read()
        self.assertEqual(content, "[]")

    def test_empty_list_rectangle(self):
        """Passing an empty list should save an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as jsonfile:
            content = jsonfile.read()
        self.assertEqual(content, "[]")

    def test_overwrites_existing_file(self):
        """save_to_file should overwrite any existing file."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        Rectangle.save_to_file([Rectangle(2, 2), Rectangle(3, 3)])
        with open("Rectangle.json", "r") as jsonfile:
            content = json.loads(jsonfile.read())
        self.assertEqual(len(content), 2)

    def test_square_filename(self):
        """Square instances should be saved to Square.json."""
        Square.save_to_file([Square(5)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_none_saves_empty_list_square(self):
        """Passing None should save an empty list for Square."""
        Square.save_to_file(None)
        with open("Square.json", "r") as jsonfile:
            content = jsonfile.read()
        self.assertEqual(content, "[]")

    def test_empty_list_square(self):
        """Passing an empty list should save an empty list for Square."""
        Square.save_to_file([])
        with open("Square.json", "r") as jsonfile:
            content = jsonfile.read()
        self.assertEqual(content, "[]")


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle(self):
        """create should rebuild a Rectangle from its dictionary."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """create should rebuild a Square from its dictionary."""
        s1 = Square(3, 1, 2, 5)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_no_file_returns_empty_list(self):
        """If the file doesn't exist, an empty list is returned."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_round_trip_rectangle(self):
        """Saving then loading should reproduce equivalent instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in loaded], [str(r1), str(r2)])

    def test_round_trip_square(self):
        """Saving then loading should reproduce equivalent instances."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual([str(s) for s in loaded], [str(s1), str(s2)])


if __name__ == "__main__":
    unittest.main()
