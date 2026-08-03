# python-everything_is_object

A closer look at how Python handles objects: `id`, `type`, mutable vs
immutable types, references, aliasing, and how arguments are passed
to functions.

## Tasks

| File | Description |
| --- | --- |
| `0-answer.txt` | Function used to print the type of an object |
| `1-answer.txt` | Function used to get a variable's identifier (memory address) |
| `2-answer.txt` | Do `a = 89` and `b = 100` point to the same object? |
| `3-answer.txt` | Do `a = 89` and `b = 89` point to the same object? |
| `4-answer.txt` | Do `a = 89` and `b = a` point to the same object? |
| `5-answer.txt` | Do `a = 89` and `b = a + 1` point to the same object? |
| `6-answer.txt` | Output of `s1 == s2` after `s2 = s1` |
| `7-answer.txt` | Output of `s1 is s2` after `s2 = s1` |
| `8-answer.txt` | Output of `s1 == s2` for two identical string literals |
| `9-answer.txt` | Output of `s1 is s2` for two identical string literals |
| `10-answer.txt` | Output of `l1 == l2` for two identical list literals |
| `11-answer.txt` | Output of `l1 is l2` for two identical list literals |
| `12-answer.txt` | Output of `l1 == l2` after `l2 = l1` |
| `13-answer.txt` | Output of `l1 is l2` after `l2 = l1` |
| `14-answer.txt` | Output after `l1.append(4)` when `l2 = l1` |
| `15-answer.txt` | Output after `l1 = l1 + [4]` when `l2 = l1` |
| `16-answer.txt` | Output after passing an int to a function that increments it |
| `17-answer.txt` | Output after passing a list to a function that appends to it |
| `18-answer.txt` | Output after passing a list to a function that reassigns it |
| `19-copy_list.py` | Function that returns a copy of a list |
| `20-answer.txt` | Is `a = ()` a tuple? |
| `21-answer.txt` | Is `a = (1, 2)` a tuple? |
| `22-answer.txt` | Is `a = (1)` a tuple? |
| `23-answer.txt` | Is `a = (1, )` a tuple? |
| `24-answer.txt` | Output of `a is b` for `a = (1)` and `b = (1)` |
| `25-answer.txt` | Output of `a is b` for `a = (1, 2)` and `b = (1, 2)` |
| `26-answer.txt` | Output of `a is b` for `a = ()` and `b = ()` |
| `27-answer.txt` | Does `id(a)` stay the same after `a = a + [5]`? |
| `28-answer.txt` | Does `id(a)` stay the same after `a += [4]`? |

## Requirements

- All Python scripts run on Ubuntu 20.04 LTS with `python3` (version 3.8.5)
- All scripts start with `#!/usr/bin/python3`
- All files end with a newline
- Code follows `pycodestyle` (version 2.7.*)
- All files are executable
- `.txt` answer files contain a single line, no shebang
