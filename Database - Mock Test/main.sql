--
SELECT e.eventName AS 'Event Name',
s.name AS 'Shop Name',
e.maxAttendees AS 'Max Attendees', 
e.eventDate AS 'Event Date'
FROM Event e, Shop s
WHERE e.shopID = s.shopID;