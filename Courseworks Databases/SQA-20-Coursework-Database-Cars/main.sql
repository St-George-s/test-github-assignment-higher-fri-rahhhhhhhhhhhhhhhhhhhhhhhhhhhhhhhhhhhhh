-- SELECT g.garageName, SUM(j.cost) AS "Total Sales"
-- FROM Garage g 
-- JOIN Job j ON g.garageID = j.garageID
-- WHERE j.dateOut = "19-Jan-20"
-- GROUP BY g.garageID;


SELECT MAX(j.dateOut - j.dateIn) AS "Number of days", j.regNo, g.garageName
FROM Job j 
JOIN Garage g ON j.garageID = g.garageID;

