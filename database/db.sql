CREATE TABLE ticket (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    case VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    severity INTEGER NOT NULL,
    result VARCHAR(255) NOT NULL,
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    display_name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    clearance INTEGER NOT NULL,
);

CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    time CURRENT_TIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    host VARCHAR(255) NOT NULL,
    link VARCHAR(255),
);