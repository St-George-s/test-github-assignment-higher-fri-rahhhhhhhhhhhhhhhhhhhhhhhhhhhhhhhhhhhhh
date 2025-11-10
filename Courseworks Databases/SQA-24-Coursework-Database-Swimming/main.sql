-- question 2c
-- SELECt s.initial, s.surname, s.swimCategory, t.teamName, COUNT(r.position) AS 'Races won'
-- FROM Swimmer s
-- JOIN Team t ON t.teamRef = s.teamRef
-- JOIN Result r ON r.swimmerID = s.swimmerID
-- WHERE r.position = 1
-- GROUP BY s.swimmerID
-- ORDER BY s.initial ASC;

SELECT s.initial, s.surname, t.teamName, e.city, e.eventDate
FROM Event e  
JOIN Race rac ON e.eventID = rac.eventID
JOIN Result res ON 