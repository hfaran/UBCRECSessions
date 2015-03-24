-------------------
-- Create Tables --
-------------------
CREATE TABLE Employees (
  sin      TEXT PRIMARY KEY,
  fName    TEXT,
  lName    TEXT,
  username TEXT,
  password TEXT,
  salt     TEXT
);
CREATE TABLE Working (
  sin         TEXT,
  start_shift INTEGER,
  end_shift   INTEGER,
  PRIMARY KEY (sin, start_shift, end_shift),
  FOREIGN KEY (sin) REFERENCES Employees
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
CREATE TABLE Session (
  session_id INTEGER PRIMARY KEY AUTOINCREMENT,
  start_time INTEGER,
  end_time   INTEGER,
  sport_id   INTEGER,
  venue_name TEXT,
  results    TEXT,
  FOREIGN KEY (sport_id) REFERENCES Sport,
  FOREIGN KEY (venue_name) REFERENCES Venue
);
CREATE TABLE Player (
  name        TEXT,
  student_num INTEGER PRIMARY KEY,
  password    TEXT,
  salt        TEXT
);
CREATE TABLE PlaysIn (
  student_num INTEGER,
  team_id     INTEGER,
  PRIMARY KEY (student_num, team_id)
);
CREATE TABLE Team_ParticipatesIn (
  team_ID           INTEGER PRIMARY KEY AUTOINCREMENT,
  name              TEXT,
  number_of_players INTEGER,
  sport_id          INTEGER,
  session_id        INT,
  venue_name        TEXT,
  FOREIGN KEY (session_id) REFERENCES Session,
  FOREIGN KEY (sport_id) REFERENCES Sport,
  FOREIGN KEY (venue_name) REFERENCES Venue
);
