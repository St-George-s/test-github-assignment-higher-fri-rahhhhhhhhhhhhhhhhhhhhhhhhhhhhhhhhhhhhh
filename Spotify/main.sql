-- DELETE FROM Tracks 
-- WHERE track_id = 5;

-- DELETE FROM Artists 
-- WHERE artist_id BETWEEN 20 AND 25;

-- INSERT INTO Genres (genre_id, genre_name) 
-- VALUES (21, 'Jazz');

-- INSERT INTO Tracks (track_id, track_name, artist_id, album_id, genre_id, duration_ms) 
-- VALUES (54, 'New Track', 4, 4, 1, 180000), 
--        (55, 'Another Track', 5, 5, 2, 200000);

-- UPDATE Albums 
-- SET release_year = 2021 
-- WHERE album_id = 3;

-- UPDATE Artists 
-- SET artist_name = 'New Artist Name' 
-- WHERE artist_id IN (1, 2, 3);

-- DELETE FROM Albums 
-- WHERE album_id = 11;

-- SELECT *
-- FROM Albums;

-- INSERT INTO Artists (artist_id, artist_name)
-- VALUES (43, 'jdfsdfsds');

-- UPDATE Tracks
-- SET duration_ms = 50
-- WHERE track_id = 4;

-- DELETE FROM Tracks
-- WHERE duration_ms <120000;

-- INSERT INTO Albums (album_id, album_name, release_year)
-- VALUES (80, 'hudahuadhu', 2030);

UPDATE Tracks
SET 