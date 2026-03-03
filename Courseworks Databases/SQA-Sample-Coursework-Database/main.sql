-- SELECT c.firstName, c.surname, v.voucherID, ROUND(co.quantityPurchased * v.price) AS "Amount of Money Spent on Voucher £"
-- FROM Customer c
-- JOIN CustomerOrder co ON c.custID = co.custID
-- JOIN Voucher v ON co.voucherID = v.voucherID
-- WHERE v.category = "Adventure"
-- AND v.voucherName LIKE "%escape room%"
-- GROUP BY co.custID
-- ORDER BY v.voucherID ASC;


-- SELECT v.voucherID, s.supplierName, v.voucherName, v.quantityAvailable - SUM(co.quantityPurchased) AS "Still Available"
-- FROM Voucher v
-- JOIN Supplier s ON v.supplierCode = s.supplierCode
-- JOIN CustomerOrder co ON v.voucherID = co.voucherID
-- WHERE v.voucherID = "V543";


SELECT s.supplierName, v.voucherName, v.price, COUNT(co.custID) AS "Number of Customers"
FROM Supplier s
JOIN Voucher v ON s.supplierCode = v.supplierCode
JOIN CustomerOrder co ON v.voucherID = co.voucherID
WHERE v.category = "Family"
AND v.price < 15
GROUP BY v.voucherName
ORDER BY COUNT(co.custID) DESC;