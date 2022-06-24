-- Forward engineer the dojos_and_ninjas_schema from the previous chapter
USE dojos_and_ninjas_schema;
-- Query: Create 3 new dojos
INSERT INTO dojos(name)
VALUES ('Cobra Kai'), ('Miyagi-Do'), ('Eagle Fang');
-- Query: Delete the 3 dojos you just created
DELETE FROM dojos
WHERE id < 4;
-- Query: Create 3 more dojos
INSERT INTO dojos(name)
VALUES ('Cobra Kai'), ('Miyagi-Do'), ('Eagle Fang');
-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas(dojo_id, first_name, last_name, age)
VALUES (4, 'Hanzo', 'Hasashi', 53), (4, 'Kuai', 'Liang', 47), (4, 'Tomas', 'Vrbada', 40);
-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas(dojo_id, first_name, last_name, age)
VALUES (5, 'Nariyoshi', 'Miyagi', 74), (5, 'Daniel', 'LaRusso', 17), (5, 'Chozen', 'Toguchi', 20);
-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas(dojo_id, first_name, last_name, age)
VALUES (6, 'Master', 'Splinter', 92), (6, 'Leonardo', 'da Vinci', 15), (6, 'Raphael', 'Sanzio', 16);
-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM dojos
LEFT JOIN ninjas 
ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 4;
-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM dojos
LEFT JOIN ninjas
ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 6;
-- Query: Retrieve the last ninja's dojo
SELECT *
FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);