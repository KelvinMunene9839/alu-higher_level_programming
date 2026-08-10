# Python - Test-driven development

This project introduces test-driven development in Python: writing
interactive doctests, unittests, and documenting modules and functions
well enough that the documentation itself can be verified.

## Topics covered

- Why tests are important
- Interactive tests (doctests) and how to write them
- Documenting modules and functions
- The basic option flags used to run tests
- Finding and covering edge cases

## Files

- `0-add_integer.py` / `tests/0-add_integer.txt` - adds two integers
- `2-matrix_divided.py` / `tests/2-matrix_divided.txt` - divides every
  element of a matrix
- `3-say_my_name.py` / `tests/3-say_my_name.txt` - prints a full name
- `4-print_square.py` / `tests/4-print_square.txt` - prints a square of
  `#` characters
- `5-text_indentation.py` / `tests/5-text_indentation.txt` - prints text
  with extra indentation after `.`, `?` and `:`
- `6-max_integer.py` / `tests/6-max_integer_test.py` - finds the max
  integer in a list, tested with `unittest`

## Requirements

- Each script starts with `#!/usr/bin/python3` and is executable
- Interactive tests live in `tests/*.txt` and run with
  `python3 -m doctest ./tests/*`
- The `max_integer` unittest runs with
  `python3 -m unittest tests.6-max_integer_test`

## Notes

These exercises are part of the ALU higher level programming curriculum
and focus on writing and documenting tests alongside the code they cover.
