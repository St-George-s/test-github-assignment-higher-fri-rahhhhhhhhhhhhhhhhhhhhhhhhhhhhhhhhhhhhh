-- SELECT c.forename, c.surname, (b.adultTicket*5.50)+(b.childTicket *2.0)+(b.concessionTicket*1.5) AS "Tax (£)"
-- FROM Customer c
-- JOIN Booking b ON c.customerID = b.customerID
-- WHERE c.customerID = "GR01932" AND b.flightID = "QH182";

SELECT MAX(childTicket) AS "maxChildren"
FROM Booking

SELECT c.forename, c.surname
FROM Customer c 
JOIN Booking b ON c.customerID = b.customerID
WHERE b.childTicket
GROUP BY c.customerID;