-- Creates a table users
-- users: id, name, email
-- id is the primary key
-- email is unique

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
