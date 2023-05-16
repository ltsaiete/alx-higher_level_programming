-- displays the top 3 of cities temperature during July and August
-- ordered by temperature (descending)
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
WHERE month >= 7 AND month <= 8
LIMIT 3
GROUP BY city
ORDER BY temperature DESC;
