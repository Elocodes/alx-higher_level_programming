-- script lists only two columns in second_table, score, name
-- Dont list rows that do not have a name value
-- output is to be ordered by score in descending order

SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
