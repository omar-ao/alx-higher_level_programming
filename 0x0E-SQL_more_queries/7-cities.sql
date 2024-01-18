-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) 
-- creates database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the above database
USE hbtn_0d_usa;
-- creates the table cities int the above database
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
	state_id INT NOT NULL FOREIGN KEY,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES state(id)
);

