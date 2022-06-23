-- Connected to the world database
USE world;
-- Try the queries that you would need to make a CRUD application (create, read, update, delete).
-- CREATE / INSERT INSERT INTO `world`.`countrylanguage` (`CountryCode`, `Language`, `IsOfficial`, `Percentage`) VALUES ('USA', 'Python', 'T', '25.0');
INSERT INTO countrylanguage(CountryCode, Language, IsOfficial, Percentage)
VALUES ('USA', 'Python', 'T', '25.0');
-- READ / SELECT
SELECT name, ROUND(population/1000000, 1) AS population FROM country ORDER BY population DESC;
-- UPDATE 
UPDATE countrylanguage SET
Percentage = 30.0
WHERE CountryCode = 'USA' AND Language = 'Python';
-- DELETE 
DELETE FROM countrylanguage
WHERE CountryCode = 'USA' AND Language = 'Python';
-- Confirm changes 
SELECT * FROM countrylanguage WHERE CountryCode = "USA";