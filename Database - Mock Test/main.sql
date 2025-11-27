--3.1
-- SELECT e.eventName AS 'Event Name',
-- s.name AS 'Shop Name',
-- e.maxAttendees AS 'Max Attendees', 
-- e.eventDate AS 'Event Date'
-- FROM Event e, Shop s
-- WHERE e.shopID = s.shopID;


--3.2
-- SELECT s.name AS 'Shop Name', e.eventName AS 'Event Name'
-- FROM Shop s
-- JOIN Event e ON e.shopID = s.shopID
-- WHERE e.eventDate = '2024-12-25';


--3.3
-- UPDATE OpeningTime
-- SET closeTime = '19:00'
-- WHERE shopID = '2';


--4.1
-- SELECT s.name AS 'Shop Name', COUNT(b.bookingID) AS 'Total Bookings'
-- FROM Shop s
-- JOIN Event e ON s.shopID = e.shopID
-- JOIN Booking b ON e.eventID = b.eventID
-- GROUP BY s.name;