-- Import in hbtn_0c_0 database this table dump: (same as Temperatures #0)
-- Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg(value) DESC
LIMIT 3;
