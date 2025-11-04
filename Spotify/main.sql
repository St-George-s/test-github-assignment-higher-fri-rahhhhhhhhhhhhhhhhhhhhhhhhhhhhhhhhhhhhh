-- SELECT * 
-- FROM Tracks 
-- WHERE album_id IN (
--   SELECT album_id 
--   FROM Albums 
--   WHERE release_year > 2018
--  );

-- SELECT T.track_name, A.album_name 
-- FROM Tracks T, Albums A
-- WHERE T.album_id = A.album_id
-- AND A.release_year > 2020;

SELECT T.track_name, A.album_name 
FROM Tracks T 
JOIN Albums A ON T.album_id = A.album_id 
WHERE A.release_year > 2020;