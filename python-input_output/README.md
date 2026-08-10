# Python - Input/Output

This project covers reading from and writing to files in Python, as well as
JSON serialization and deserialization.

## Topics covered

- Opening, reading, and writing text files
- Using the `with` statement for automatic file closing
- Serializing Python data structures to JSON and back
- Persisting objects to disk as JSON and reloading them
- Building a simple serialization/deserialization mechanism for a class

## Files

- `0-read_file.py` - reads a text file and prints its content to stdout
- `1-write_file.py` - writes a string to a text file
- `2-append_write.py` - appends a string to the end of a text file
- `3-to_json_string.py` - returns the JSON representation of an object
- `4-from_json_string.py` - returns an object from a JSON string
- `5-save_to_json_file.py` - writes an object to a file as JSON
- `6-load_from_json_file.py` - creates an object from a JSON file
- `7-add_item.py` - adds all its arguments to a list saved as JSON
- `8-class_to_json.py` - returns the dictionary description of a simple
  object instance
- `9-student.py` - `Student` class with a `to_json` method
- `10-student.py` - `Student` class with a filterable `to_json` method
- `11-student.py` - `Student` class supporting JSON reload via
  `reload_from_json`
- `12-pascal_triangle.py` - builds Pascal's triangle

## Requirements

- Python 3.8+
- Files should follow the project style requirements
- Each script should start with `#!/usr/bin/python3`

## Notes

These exercises are part of the ALU higher level programming curriculum and
focus on file I/O and JSON serialization/deserialization in Python.
