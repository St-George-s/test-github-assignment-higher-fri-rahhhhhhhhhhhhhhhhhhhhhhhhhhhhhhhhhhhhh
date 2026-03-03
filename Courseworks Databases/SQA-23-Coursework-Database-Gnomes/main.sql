-- 2b
-- SELECT g.gnomeName, SUM(gp.quantity) AS 'Total gnomes sold'
-- FROM Gnome g
-- JOIN GnomePurchase gp ON g.gnomeID = gp.gnomeID
-- WHERE g.description LIKE '%solar%'
-- GROUP BY gnomeName
-- ORDER BY SUM(quantity) DESC;


-- 2c
-- SELECT c.emailAddress, o.orderID, gp.quantity
-- FROM Customer c
-- JOIN Orders o ON c.customerID = o.customerID
-- JOIN GnomePurchase gp ON o.orderID = gp.orderID
-- JOIN Gnome g ON gp.gnomeID = g.gnomeID
-- WHERE gp.quantity >=3
-- AND g.unitPrice = (
--     SELECT max(unitPrice)
--     FROM Gnome
-- ) ;


-- 2d
-- SELECT forename, surname, round(SUM(quantity * unitPrice * 1.2),2) AS [Total to pay £]
-- FROM Customer, Gnome, GnomePurchase, Orders
-- WHERE Orders.orderID = "ord0024"
-- AND Customer.customerID = Orders.customerID
-- AND Orders.orderID = GnomePurchase.orderID
-- AND Gnome.gnomeID = GnomePurchase.gnomeID;
 