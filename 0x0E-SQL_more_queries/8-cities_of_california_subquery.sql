-- script that lists all the cities of California that can be found in the database
USE hbtn_0d_usa;

-- Find the id of California
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- List all cities in California, sorted by cities.id
SELECT * FROM cities WHERE state_id = @california_id ORDER BY id ASC;

