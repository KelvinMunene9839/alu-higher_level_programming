# Python - Almost a circle

This project builds a small class hierarchy (`Base` -> `Rectangle` ->
`Square`) with full attribute validation, unit tests, and JSON
serialization/deserialization, to practice unit testing, `*args`/
`**kwargs`, and packaging code into modules.

## Topics covered

- Unit testing, and how to implement it in a large project
- Serializing and deserializing a class to/from JSON
- Reading and writing JSON files
- `*args` and `**kwargs`
- Handling named arguments in a function

## Project layout

- `models/__init__.py` - makes `models` a Python package
- `models/base.py` - the `Base` class: id management and JSON
  (de)serialization (`to_json_string`, `from_json_string`,
  `save_to_file`, `load_from_file`, `create`)
- `models/rectangle.py` - the `Rectangle` class: validated
  `width`/`height`/`x`/`y`, `area`, `display`, `__str__`, `update`,
  `to_dictionary`
- `models/square.py` - the `Square` class, inheriting from `Rectangle`,
  with a `size` property and its own `__str__`, `update` and
  `to_dictionary`
- `tests/test_models/` - the unit test suite, mirroring the `models/`
  layout

## Requirements

- Each script starts with `#!/usr/bin/python3` and is executable
- Tests run with `python3 -m unittest discover tests`, or file by file
  with `python3 -m unittest tests/test_models/test_base.py`

## Notes

These exercises are part of the ALU higher level programming curriculum
and focus on writing thoroughly unit-tested, well-documented Python
classes.
