# SQL - Introduction

This project introduces the basics of MySQL: creating and dropping
databases, creating tables, and reading/writing/updating/deleting rows.

## Topics covered

- Listing, creating, and dropping databases
- Listing tables and inspecting a table's structure
- Creating tables and inserting rows
- Selecting, filtering, ordering, and grouping rows
- Updating and deleting rows

## Files

- `0-list_databases.sql` - lists all databases
- `1-create_database_if_missing.sql` - creates the database `hbtn_0c_0`
  if it doesn't already exist
- `2-remove_database.sql` - deletes the database `hbtn_0c_0` if it exists
- `3-list_tables.sql` - lists all tables of a database
- `4-first_table.sql` - creates the table `first_table`
- `5-full_table.sql` - prints the full description of `first_table`
- `6-list_values.sql` - lists all rows of `first_table`
- `7-insert_value.sql` - inserts a new row into `first_table`
- `8-count_89.sql` - counts records with `id = 89` in `first_table`
- `9-full_creation.sql` - creates `second_table` and inserts rows
- `10-top_score.sql` - lists records of `second_table` ordered by score
- `11-best_score.sql` - lists records of `second_table` with score >= 10
- `12-no_cheating.sql` - updates Bob's score by name only
- `13-change_class.sql` - deletes records with score <= 5
- `14-average.sql` - computes the average score
- `15-groups.sql` - counts records grouped by score
- `16-no_link.sql` - lists records with a non-null name, by descending score

## Requirements

- All scripts are run on the MySQL server via
  `cat <file>.sql | mysql -hlocalhost -uroot -p [database]`
- Each script performs its task without failing if run more than once,
  where applicable

## Notes

These exercises are part of the ALU higher level programming curriculum
and focus on the fundamentals of MySQL/SQL.
