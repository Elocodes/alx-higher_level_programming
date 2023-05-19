-- script creates a table called "first_table in the current database
-- of my MySql server. The database name will be passed as argument
-- of the command

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256) );
