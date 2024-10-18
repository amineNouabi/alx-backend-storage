-- Create a table users with the following columns:
-- id, email, name, country
-- id is an integer, primary key, auto increment
-- email is a string, not null, unique
-- name is a string
-- country is an enum that can be 'US', 'CO', or 'TN' and has a default value of 'US'

CREATE TYPE country AS ENUM ('US', 'CO', 'TN');

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country country NOT NULL DEFAULT 'US'
);
