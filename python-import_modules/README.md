# python-import_modules

Python fundamentals: importing functions and variables from other files,
creating modules, using `dir()`, guarding a script's top-level code with
`if __name__ == "__main__":` so it isn't executed on import, and reading
command line arguments with `sys.argv`.

## Tasks

| File | Description |
| --- | --- |
| `add_0.py` | Module defining `add(a, b)`, imported by `0-add.py` |
| `0-add.py` | Imports `add` from `add_0` and prints `1 + 2 = 3` |
| `calculator_1.py` | Module defining `add`, `sub`, `mul`, `div` |
| `1-calculation.py` | Imports the four functions and prints each result |
| `2-args.py` | Prints the number of arguments and lists them |
| `3-infinite_add.py` | Prints the sum of all command line arguments |
| `variable_load_5.py` | Module defining the variable `a = 98` |
| `4-hidden_discovery.py` | Prints every public name defined in `hidden_4.pyc` |
| `5-variable_load.py` | Imports `a` from `variable_load_5` and prints it |

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Style checked with `pycodestyle` 2.7.*
- Every file starts with `#!/usr/bin/python3` and is executable
- No `import *` or `__import__` used for the import tasks
- Each script guards its executable code with `if __name__ == "__main__":`
  so nothing runs when the module is imported elsewhere
