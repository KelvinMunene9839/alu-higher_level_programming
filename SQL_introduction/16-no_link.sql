-- Lists all records of second_table with a name value,
-- displaying score and name, ordered by descending score
SELECT score, name FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;
