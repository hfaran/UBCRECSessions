-------------------
-- Create Tables --
-------------------
CREATE TABLE Employees (
    sin TEXT, fName TEXT, lName TEXT, username TEXT,
    password TEXT, salt TEXT
);
CREATE TABLE Working (sin TEXT, startShift TEXT, endShift TEXT);
CREATE TABLE Venue (name TEXT, address TEXT);
CREATE TABLE Sport (name TEXT, sportID INT);
CREATE TABLE Session (
    start_time INTEGER, end_time INTEGER,
    session_id UNSIGNED INT, sport_id UNSIGNED INT, venue_name TEXT,
    results TEXT
);
CREATE TABLE Player (
    name TEXT , student_num UNSIGNED INT,
    password TEXT, salt TEXT
);
CREATE TABLE PlaysIn (student_num UNSIGNED INT, team_id UNSIGNED INT);
CREATE TABLE Team_ParticipatesIn (
    name TEXT, team_ID UNSIGNED INT, number_of_players UNSIGNED INT,
    sport_id UNSIGNED INT, session_id INT,venue_name TEXT
);
