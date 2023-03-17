-- This script create a new table with some arguments and set the default value of the if to 1
CREATE TABLE IF NOT EXISTS id_not_null(
    id INTEGER DEFAULT 1,
    name VARCHAR(256)
);