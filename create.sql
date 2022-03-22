CREATE DATABASE sample
    DEFAULT CHARACTER SET = 'utf8mb4';
use sample;

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id        varchar(32) not null PRIMARY KEY,
  name       varchar(50) not null,
  email       varchar(50) not null
);
SET FOREIGN_KEY_CHECKS=1;

INSERT INTO students VALUES ('G12345678', 'Jett Jacobs', 'jacobsemail@fakeemail.com');
INSERT INTO students VALUES ('G22489071', 'Alex Coleman', 'alexcoleman@fakeemail.com');
INSERT INTO students VALUES ('G82915273', 'Ethan Baron', 'ethan@fakeemail.com');
INSERT INTO students VALUES ('G22004676', 'Cat Meadows', 'cat@fakeemail.com');

UPDATE students SET name = 'Catherine Meadows' WHERE id = 'G22004676';