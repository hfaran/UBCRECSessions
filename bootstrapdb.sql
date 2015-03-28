-------------------
-- Create Tables --
-------------------

CREATE TABLE Employees (
  sin        TEXT PRIMARY KEY,
  first_name TEXT,
  last_name  TEXT,
  username   TEXT,
  password   TEXT,
  salt       TEXT
);
CREATE TABLE Working (
  sin         TEXT,
  start_shift INTEGER,
  end_shift   INTEGER,
  PRIMARY KEY (sin, start_shift, end_shift),
  FOREIGN KEY (sin) REFERENCES Employees (sin)
);
CREATE TABLE Venue (
  name    TEXT PRIMARY KEY,
  address TEXT
);
CREATE TABLE Sport (
  sport_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name     TEXT,
  UNIQUE (name)
);
CREATE TABLE Sessions (
  session_id INTEGER PRIMARY KEY AUTOINCREMENT,
  start_time INTEGER,
  end_time   INTEGER,
  sport_id   INTEGER,
  venue_name TEXT,
  results    TEXT,
  FOREIGN KEY (sport_id) REFERENCES Sport (sport_id),
  FOREIGN KEY (venue_name) REFERENCES Venue (venue_name)
);
CREATE TABLE Players (
  name        TEXT,
  student_num INTEGER PRIMARY KEY,
  password    TEXT,
  salt        TEXT
);
CREATE TABLE PlaysIn (
  student_num INTEGER,
  team_id     INTEGER,
  PRIMARY KEY (student_num, team_id),
  FOREIGN KEY (student_num) REFERENCES Players (student_num),
  FOREIGN KEY (team_id) REFERENCES Team_ParticipatesIn (team_id)
);
CREATE TABLE Team_ParticipatesIn (
  team_id           INTEGER PRIMARY KEY AUTOINCREMENT,
  name              TEXT,
  number_of_players INTEGER,
  session_id        INT,
  FOREIGN KEY (session_id) REFERENCES Sessions (session_id)
);


-----------------
-- Insert Data --
-----------------

INSERT INTO Employees (sin, first_name, last_name, username, password, salt)
VALUES (11111111, 'Antoinette', 'Calhoon', 'acalhoon',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');
INSERT INTO Employees (sin, first_name, last_name, username, password, salt)
VALUES (22222222, 'Jennie', 'Bucko', 'jbucko',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');
INSERT INTO Employees (sin, first_name, last_name, username, password, salt)
VALUES (33333333, 'Lizabeth', 'Ringdahl', 'lringdahl',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');
INSERT INTO Employees (sin, first_name, last_name, username, password, salt)
VALUES (44444444, 'Georgeann', 'Lenoir', 'glenoir',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');
INSERT INTO Employees (sin, first_name, last_name, username, password, salt)
VALUES (55555555, 'Romeo', 'Calhoon', 'rcalhoon',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');

INSERT INTO Working (sin, start_shift, end_shift)
VALUES (11111111, 1427235705, 1427239305);
INSERT INTO Working (sin, start_shift, end_shift)
VALUES (22222222, 1427235705, 1427239305);
INSERT INTO Working (sin, start_shift, end_shift)
VALUES (33333333, 1427235705, 1427239305);
INSERT INTO Working (sin, start_shift, end_shift)
VALUES (44444444, 1427235705, 1427239305);
INSERT INTO Working (sin, start_shift, end_shift)
VALUES (55555555, 1427235705, 1427239305);

INSERT INTO Venue (name, address)
VALUES ('SRC_A', '2329 West Mall, Vancouver, BC');
INSERT INTO Venue (name, address)
VALUES ('SRC_B', '2329 West Mall, Vancouver, BC');
INSERT INTO Venue (name, address)
VALUES ('Thunderbird', '2330 Thunderbird Boulevard, Vancouver, BC');
INSERT INTO Venue (name, address)
VALUES ('Aquatic_Center', '6121 University Boulevard Vancouver, BC');
INSERT INTO Venue (name, address)
VALUES ('SRC_GYM', '2329 West Mall, Vancouver, BC');

INSERT INTO Sport (name) VALUES ('Indoor Soccer');
INSERT INTO Sport (name) VALUES ('Basketball');
INSERT INTO Sport (name) VALUES ('Volleyball');
INSERT INTO Sport (name) VALUES ('Table Tennis');
INSERT INTO Sport (name) VALUES ('Croquet');

INSERT INTO Sessions (start_time, end_time, sport_id, venue_name)
VALUES (1427235705, 1427239305, 1, 'SRC_A');
INSERT INTO Sessions (start_time, end_time, sport_id, venue_name)
VALUES (1427235705, 1427239305, 2, 'SRC_B');
INSERT INTO Sessions (start_time, end_time, sport_id, venue_name)
VALUES (1427235705, 1427239305, 3, 'Thunderbird');
INSERT INTO Sessions (start_time, end_time, sport_id, venue_name)
VALUES (1427235705, 1427239305, 4, 'SRC_GYM');
INSERT INTO Sessions (start_time, end_time, sport_id, venue_name)
VALUES (1427235705, 1427239305, 5, 'Aquatic_Center');

INSERT INTO Players (student_num, name, password, salt)
VALUES (12346589, 'Patton Hunt',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');
INSERT INTO Players (student_num, name, password, salt)
VALUES (09876543, 'Ehsan Obama',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');
INSERT INTO Players (student_num, name, password, salt)
VALUES (67539489, 'Niles Lemieux',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');
INSERT INTO Players (student_num, name, password, salt)
VALUES (68723732, 'Isaiah Nearan',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');
INSERT INTO Players (student_num, name, password, salt)
VALUES (89789656, 'Sarah Blessnil',
        '$2a$12$SyAcf3XD/hg0fLEbAPahheWyrHGORDRbgb6zTyQPpI/i4clYj.kau',
        '$2a$12$SyAcf3XD/hg0fLEbAPahhe');

INSERT INTO Team_ParticipatesIn (name, team_id, number_of_players, session_id)
VALUES ('Lakers', 1, 10, 1);
INSERT INTO Team_ParticipatesIn (name, team_id, number_of_players, session_id)
VALUES ('Canucks', 2, 10, 2);
INSERT INTO Team_ParticipatesIn (name, team_id, number_of_players, session_id)
VALUES ('MU', 3, 10, 3);
INSERT INTO Team_ParticipatesIn (name, team_id, number_of_players, session_id)
VALUES ('Fake Madrid', 4, 10, 4);
INSERT INTO Team_ParticipatesIn (name, team_id, number_of_players, session_id)
VALUES ('Eagles', 5, 10, 5);

INSERT INTO PlaysIn (student_num, team_id) VALUES (12346589, 1);
INSERT INTO PlaysIn (student_num, team_id) VALUES (12346589, 2);
INSERT INTO PlaysIn (student_num, team_id) VALUES (12346589, 3);
INSERT INTO PlaysIn (student_num, team_id) VALUES (09876543, 2);
INSERT INTO PlaysIn (student_num, team_id) VALUES (09876543, 3);
INSERT INTO PlaysIn (student_num, team_id) VALUES (09876543, 4);
INSERT INTO PlaysIn (student_num, team_id) VALUES (67539489, 3);
INSERT INTO PlaysIn (student_num, team_id) VALUES (67539489, 4);
INSERT INTO PlaysIn (student_num, team_id) VALUES (67539489, 5);
INSERT INTO PlaysIn (student_num, team_id) VALUES (68723732, 4);
INSERT INTO PlaysIn (student_num, team_id) VALUES (68723732, 5);
INSERT INTO PlaysIn (student_num, team_id) VALUES (68723732, 1);
INSERT INTO PlaysIn (student_num, team_id) VALUES (89789656, 5);
INSERT INTO PlaysIn (student_num, team_id) VALUES (89789656, 1);
INSERT INTO PlaysIn (student_num, team_id) VALUES (89789656, 2);
