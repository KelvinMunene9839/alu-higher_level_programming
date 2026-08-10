#!/usr/bin/python3
"""Defines the Base class, the base of all other classes in this project."""
import json


class Base:
    """Manage the id attribute for all future classes.

    This class is the "base" of all other classes in this project,
    avoiding duplicate id-management code (and bugs) across
    subclasses.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance. If None,
                __nb_objects is incremented and used as the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: "[]" if list_dictionaries is None or empty,
                otherwise the JSON string representation of
                list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        The filename is "<cls.__name__>.json" and is overwritten if
        it already exists.

        Args:
            list_objs (list): A list of instances that inherit from
                Base. If None, an empty list is saved.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): A string representing a list of
                dictionaries.

        Returns:
            list: An empty list if json_string is None or empty,
                otherwise the list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of cls with all attributes already set.

        A "dummy" instance is created with mandatory attributes set
        to 1, then updated with the given dictionary.

        Args:
            **dictionary: Key/value pairs of attributes to set on
                the new instance.

        Returns:
            An instance of cls with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from "<cls.__name__>.json".

        Returns:
            list: An empty list if the file doesn't exist, otherwise
                a list of instances of cls built from the file's
                contents.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
        except IOError:
            return []
        return [cls.create(**d) for d in list_dicts]
