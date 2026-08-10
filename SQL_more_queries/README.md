# SQL - More queries

This project goes further into MySQL: creating users and managing their
privileges, primary and foreign keys, `NOT NULL`/`UNIQUE` constraints,
subqueries, and joining/combining data from multiple tables.

## Topics covered

- Creating MySQL users and managing their privileges
- `PRIMARY KEY` and `FOREIGN KEY` constraints
- `NOT NULL` and `UNIQUE` constraints
- Retrieving data from multiple tables in a single query
- Subqueries
- `JOIN` and `UNION`

## Files

- `0-privileges.sql` - lists all privileges of `user_0d_1` and `user_0d_2`
- `1-create_user.sql` - creates the user `user_0d_1` with all privileges
- `2-create_read_user.sql` - creates `hbtn_0d_2` and a read-only user
- `3-force_name.sql` - creates `force_name`, where `name` can't be null
- `4-never_empty.sql` - creates `id_not_null`, where `id` defaults to 1
- `5-unique_id.sql` - creates `unique_id`, where `id` is unique
- `6-states.sql` - creates `hbtn_0d_usa` and the `states` table
- `7-cities.sql` - creates the `cities` table, linked to `states`
- `8-cities_of_california_subquery.sql` - cities of California, via subquery
- `9-cities_by_state_join.sql` - cities and their state name, via `JOIN`
- `10-genre_id_by_show.sql` - shows that have at least one genre linked
- `11-genre_id_all_shows.sql` - all shows and their genre_id (NULL if none)
- `12-no_genre.sql` - shows without a linked genre
- `13-count_shows_by_genre.sql` - number of shows per genre
- `14-my_genres.sql` - all genres of the show Dexter
- `15-comedy_only.sql` - all shows in the Comedy genre
- `16-shows_by_genre.sql` - all shows and their linked genre names

Tasks 10-16 use the `hbtn_0d_tvshows` database dump.

## Requirements

- All scripts are run on the MySQL server via
  `cat <file>.sql | mysql -hlocalhost -uroot -p [database]`
- SQL keywords are written in uppercase
- Every query is preceded by a comment, and every file starts with a
  comment describing its task

## Notes

These exercises are part of the ALU higher level programming curriculum
and focus on MySQL users/privileges, constraints, and multi-table queries.
