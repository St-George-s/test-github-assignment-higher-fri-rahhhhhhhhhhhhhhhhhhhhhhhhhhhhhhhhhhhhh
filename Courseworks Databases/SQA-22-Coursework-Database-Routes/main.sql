-- 2b
SELECT p.forename, p.surname, p.plannerNo, count(w.walkID)
FROM Planner p
JOIN Route r ON p.plannerNo = r.plannerNo
JOIN 
