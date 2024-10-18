-- Creates a table users
-- users: id, name, email
-- id is the primary key
-- email is unique
-- name and email are not null

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE
);
