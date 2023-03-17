-- This script create a new database and a new table in the new database and Make the id unique, auto generated and primary key
-- and state_id the is a FOREIGN KEY and referenced to the id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INTEGER NOT NULL AUTO_INCREMENT,
    state_id INTEGER NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);