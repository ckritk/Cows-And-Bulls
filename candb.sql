CREATE DATABASE IF NOT EXISTS candb;

USE candb;

CREATE TABLE IF NOT EXISTS data (
    NOD INT PRIMARY KEY,
    Played INT DEFAULT 0,
    Won INT DEFAULT 0,
    Lost INT DEFAULT 0,
    Record INT DEFAULT NULL,
    Time TIME DEFAULT NULL
);

INSERT INTO data (NOD, Played, Won, Lost, Record, Time) VALUES
(3, 0, 0, 0, NULL, NULL),
(4, 0, 0, 0, NULL, NULL),
(5, 0, 0, 0, NULL, NULL),
(6, 0, 0, 0, NULL, NULL),
(7, 0, 0, 0, NULL, NULL),
(8, 0, 0, 0, NULL, NULL),
(9, 0, 0, 0, NULL, NULL),
(10, 0, 0, 0, NULL, NULL);

