-- a SQL script that creates a table users

CREATE TABLE IF NOT EXIST users (
	id INTEGER PRIMARY AUTOINCREMENT NOT NULL,
	email VARCHAR(255) NOT NULL unique,
	name VARCHAR(255)
);
