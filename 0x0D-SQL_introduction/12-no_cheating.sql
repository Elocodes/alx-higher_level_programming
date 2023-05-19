-- script updates bob's score and displays only two columns in second_table
-- output is to be ordered by score in descending order

UPDATE second_table
SET score = 10
WHERE name = 'Bob';

SELECT score, name
FROM second_table
ORDER BY score DESC;
