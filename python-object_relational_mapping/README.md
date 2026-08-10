# Python - Object-relational mapping

This project connects Python scripts to a MySQL database, first with the
low-level `MySQLdb` driver and then with the SQLAlchemy ORM, mapping
Python classes to MySQL tables.

## Topics covered

- Connecting to a MySQL database from a Python script
- `SELECT`ing and `INSERT`ing rows from a Python script
- What an ORM is
- Mapping a Python class to a MySQL table with SQLAlchemy
- SQL injection, and how to avoid it with parameterized queries

## Files

### MySQLdb

- `0-select_states.py` - lists all states
- `1-filter_states.py` - lists states whose name starts with `N`
- `2-my_filter_states.py` - lists states matching a name (SQL-injection
  prone, for comparison)
- `3-my_safe_filter_states.py` - the same, but safe from SQL injection
- `4-cities_by_state.py` - lists all cities with their state
- `5-filter_cities.py` - lists all cities of a given state

### SQLAlchemy

- `model_state.py` - the `State` class, mapped to the `states` table
- `model_city.py` - the `City` class, mapped to the `cities` table
- `6-model_state.py` - creates the `states` table from the model
- `7-model_state_fetch_all.py` - lists all `State` objects
- `8-model_state_fetch_first.py` - prints the first `State` object
- `9-model_state_filter_a.py` - lists `State` objects containing `a`
- `10-model_state_my_get.py` - prints the id of a `State` by name
- `11-model_state_insert.py` - adds a new `State`
- `12-model_state_update_id_2.py` - renames the `State` with id 2
- `13-model_state_delete_a.py` - deletes every `State` containing `a`
- `14-model_city_fetch_by_state.py` - lists all `City` objects with
  their state's name

## Requirements

- Each script takes MySQL credentials and a database name as arguments,
  connects to `localhost:3306`, and does not run its logic on import
- `MySQLdb` version 2.0.x and `SQLAlchemy` version 1.4.x

## Notes

These exercises are part of the ALU higher level programming curriculum
and focus on talking to MySQL from Python, both directly and through an
ORM.
