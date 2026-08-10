-- Creates the database hbtn_0d_usa and the table states
-- Creates the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Creates the table states if it doesn't already exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
