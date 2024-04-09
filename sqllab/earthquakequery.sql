-- Find all the earthquakes with a mag between 3 and 3.1 and put it in desc order by mag.
SELECT * FROM earthquakes WHERE mag BETWEEN 3 AND 3.1 ORDER BY mag DESC;
-- Find all the earthquakes with a quake depth between 9 and 12 and put it in desc order by quake depth.
SELECT * FROM earthquakes WHERE quakedepth BETWEEN 9 AND 12 ORDER BY quakedepth DESC;
-- Find all the earthquakes that have a depth of less than 1 and put it in desc order by quake depth.
SELECT * FROM earthquakes WHERE quakedepth<1 ORDER BY quakedepth DESC;