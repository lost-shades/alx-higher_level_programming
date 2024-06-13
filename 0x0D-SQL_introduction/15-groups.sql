-- lists the number of records with same score in a table
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC; 
