-- script lists number of records having the same score
-- the tally or count is displayed with the label 'number' 

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
