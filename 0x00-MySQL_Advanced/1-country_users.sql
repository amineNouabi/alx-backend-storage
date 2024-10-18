-- Create a table users with the following columns:
-- id, email, name, country
-- id is an integer, primary key, auto increment
-- email is a string, not null, unique
-- name is a string
-- country is an enum that can be 'US', 'CO', or 'TN' and has a default value of 'US'

DROP TYPE IF EXISTS country;
CREATE TYPE country AS ENUM ('US', 'CO', 'TN');

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country country NOT NULL DEFAULT 'US'
);
