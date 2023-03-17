-- This script create a new table with some arguments and set the default value of the if to 1 and it must me unique
CREATE TABLE IF NOT EXISTS unique_id(
    id INTEGER DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);