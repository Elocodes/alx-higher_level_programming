-- script lists only two columns in second_table and displays scores >= 10
-- output is to be ordered by score in descending order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
