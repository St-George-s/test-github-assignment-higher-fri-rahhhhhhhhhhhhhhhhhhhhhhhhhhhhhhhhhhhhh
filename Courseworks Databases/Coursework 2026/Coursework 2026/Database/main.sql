-- 2c
-- SELECT forename, surname
-- FROM Customer c
-- JOIN Purchase p ON p.customerID = c.customerID
-- JOIN Movie m ON m.movieCode = p.movieCode
-- WHERE duration = (
--     SELECT min(duration)
--     FROM Movie
-- );

-- 2d
-- SELECT forename, surname, SUM(price) AS 'Total spent (£)'
-- FROM Customer c
-- JOIN Purchase p ON p.customerID = c.customerID
-- JOIN Movie m ON m.movieCode = p.movieCode
-- WHERE genreID = 'G-04'
-- GROUP BY c.customerID
-- ORDER BY SUM(price) DESC;

-- 2e
SELECT forename, surname, email
FROM Customer, Purchase, Movie
WHERE customer.customerID = purchase.customerID
AND movie.movieCode = purchase.movieCode
AND released >= 1990 AND released <=1999
GROUP BY customer.customerID
ORDER BY forename ASC;
