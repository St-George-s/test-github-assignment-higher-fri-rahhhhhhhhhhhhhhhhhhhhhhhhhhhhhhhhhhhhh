-- question 2c
-- SELECt s.initial, s.surname, s.swimCategory, t.teamName, COUNT(r.position) AS 'Races won'
-- FROM Swimmer s
-- JOIN Team t ON t.teamRef = s.teamRef
-- JOIN Result r ON r.swimmerID = s.swimmerID
-- WHERE r.position = 1
-- GROUP BY s.swimmerID
-- ORDER BY s.initial ASC;


--2D
-- SELECT s.initial, s.surname, t.teamName, e.city, e.eventDate
-- FROM Event e  
-- JOIN Race rac ON e.eventID = rac.eventID
-- JOIN Result res ON rac.raceNumber = res.raceNumber
-- JOIN Swimmer s ON res.swimmerID = s.swimmerID
-- JOIN Team t ON s.teamRef = t.teamRef
-- WHERE res.raceTime = (
--     SELECT min(raceTime)
--     FROM Result
--     WHERE lane = 1 or lane = 8
-- );


--2e
-- SELECT teamName, COUNT(position) AS [Total medals won]
-- FROM Result, Swimmer, Team
-- WHERE Result.swimmerID = Swimmer.swimmerID 
-- AND Swimmer.teamRef = Team.teamRef
-- AND position <4
-- GROUP BY teamName
-- ORDER BY COUNT(position) DESC;


SELECT *
FROM Event;