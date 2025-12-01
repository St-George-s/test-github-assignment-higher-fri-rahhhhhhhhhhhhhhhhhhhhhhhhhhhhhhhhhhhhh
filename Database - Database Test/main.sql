-- 3.1
-- SELECT e.episodeTitle, s.showName, e.maxViewers, e.episodeDate
-- FROM Episode e
-- JOIN Show s ON e.showID = s.showID;


-- 3.2
-- SELECT s.showName AS 'Show', e.episodeTitle AS 'Episode'
-- FROM Episode e
-- JOIN Show s ON e.showID = s.showID
-- WHERE e.episodeDate LIKE '2024-12-%';


--3.3
-- UPDATE Timeslot
-- SET endTime = '19:30'
-- WHERE showID = '2';


-- PART C
-- SELECT s.showName, COUNT(v.ratingID) AS 'Total Ratings'
-- FROM Show s
-- JOIN Episode e ON s.showID = e.showID
-- JOIN ViewerRating v ON e.episodeID = v.episodeID
-- GROUP BY s.showName
-- ORDER BY COUNT(v.ratingID) DESC;