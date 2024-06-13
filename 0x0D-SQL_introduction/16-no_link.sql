-- lists all records of a table leaving rows without a name
SELECT score, name 
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
