import sqlite3

from ubcrec import models


class SQLAPI(object):
    """Abstraction for database

    :type db_path: str
    :param db_path: String containing address of the database
    """
    def __init__(self, db_path='project.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def insertEmployeesData(self, Sin, fName, lName, username, password, salt):
        """
        :type Sin: str
        :param Sin: Employees SIN number
        :type fName: str
        :param fName: First name
        :type lName:str
        :param lName: Last name
        :type username: str
        :param username: Username for employee
        :type password: str
        :param password: Password for that employee
        :type salt: str
        :param salt: salt for fun :D
        """
        self.cursor.execute(
            "INSERT INTO Employees VALUES (?, ?, ?, ?, ?, ?)",
            (Sin,
             fName,
             lName,
             username,
             password,
             salt))
        self.conn.commit()

    def insertWorkingData(self, Sin, startShift, endShift):
        """
        :type Sin: str
        :param Sin: Employees SIN number
        :type startShift: int
        :param startShift: Employees start shift (Unix Time)
        :type endShift: int
        :param endShift: Employees end shift (Unix Time)
        """
        self.cursor.execute(
            "INSERT INTO Working VALUES (? ,? ,?)",
            (Sin,
             startShift,
             endShift)
        )
        self.conn.commit()

    def create_venue(self, name, address):
        """
        :type name: str
        :param name: Venue name
        :type address: str
        :param address: address of venue
        """
        self.cursor.execute(
            "INSERT INTO Venue VALUES (? ,?)", (name, address)
        )
        self.conn.commit()

    def insertSportData(self, sportName, sportID):
        """

        :type sportName: str
        :param sportName: Name of the sport
        :type sportID: int
        :param sportID: ID of the sport type
        """
        self.cursor.execute(
            "INSERT INTO Sport VALUES (? ,?)", (sportName, sportID)
        )
        self.conn.commit()

    def create_session(self, startTime, endTime, sportID, venueName):
        """Create a new session

        :type startTime: int
        :param startTime: Start time for a session in Unix Time (seconds)
        :type endTime: int
        :param endTime: End time for a session in Unix Time (seconds)s
        :type sportID: int
        :param sportID: ID for the sport type
        :type venueName: str
        :param venueName: Name of the venue

        :returns: ID of newly created session
        :rtype: int
        """
        raise NotImplementedError

        sessionID = None  # TODO This should be auto-incremented by SQL
        results = None  # TODO Doesn't make sense to add on a PUT; should be
            # inserted afterwards; also wtf is this supposed to actually
            # represent, it isn't specified clearly anywhere.
        self.cursor.execute(
            "INSERT INTO Session VALUES (? ,?,? ,?,? ,?)",
            (startTime,
             endTime,
             sessionID,
             sportID,
             venueName,
             results)
        )
        self.conn.commit()

        # TODO Get and return session_id
        # return session_id

    def add_session_results(self, session_id, results):
        """Add results to session

        :type session_id: int
        :type results: str
        """
        raise NotImplementedError

    def insert_player_data(self, name, student_number, password, salt):
        """
        :type name: str
        :param name: Name of the student/player
        :type student_number: int
        :param student_number: Student ID of the player
        :type password: str
        :param password: Password for that student
        :type salt: str
        :param salt: Password salt
        """
        self.cursor.execute(
            "INSERT INTO Player VALUES (?,?,?,?)",
            (name,
             password,
             student_number,
             salt)
        )
        self.conn.commit()

    def insertPlaysInData(self, studentNum, teamID):
        """
        :type studentNum int
        :param studentNum: Student number of the player
        :type teamID: int
        :param teamID: Team ID
        """
        self.cursor.execute(
            "INSERT INTO PlaysIn VALUES (? ,?)", (studentNum, teamID)
        )
        self.conn.commit()

    def create_team(self, name, num_max_players, session_id):
        """Inserting data for Team_ParticipatesIn table

        :type name: str
        :param name: Name of the team
        :type num_max_players: int
        :param num_max_players: Number of player in a team
        :type session_id: int
        :param session_id: ID for session
        :rtype: int
        :returns: ID of newly created team
        """
        self.cursor.execute(
            "INSERT INTO Team_ParticipatesIn "
            "(name, number_of_players, session_id) "
            "VALUES (?,?,?)",
            (name,
             num_max_players,
             session_id)
        )
        self.conn.commit()

        # Return ID of newly created team
        return self.cursor.lastrowid

    def get_player(self, student_number):
        """Gets player with ``student_number``

        If no such player exists, return ``None``.

        :type student_number: int
        :param student_number: Student number of player to find
        :returns: Model of player with user
        :rtype: models.Player or None
        """
        raise NotImplementedError

    def get_player_session_ids(self, student_number):
        """Returns list of IDs for session that player is/was registered in

        :type student_number: int
        :param student_number: Student number of player to find
        :rtype: list
        :returns: list of session IDs
        """
        raise NotImplementedError

    def get_session(self, session_id):
        """Returns session with ``session_id``

        :type session_id: int
        :param session_id: ID of session
        :return: Session or None if no such session with ``session_id`` exists
        :rtype: models.Session or None
        """
        raise NotImplementedError

    def get_sessions(self, started_before=None, ended_before=None, sports=None,
                     venues=None):
        """Returns list of Session objects that match the provided filters

        :type started_before: int or None
        :param started_before: Filter only sessions with a start_time greater
            than this (Unix Time), or, if this is None, do not filter.
        :type ended_before: int or None
        :param ended_before: Filter only sessions with an end_time smaller
            than this (Unix Time), or, if this is None, do not filter.
        :type sports: list or None
        :param sports: List of sport names; filter only sessions for these
            sports,  or, if this is None, do not filter.
        :type venues: list or None
        :param venues: List of venue names; filter only sessions held in
            these venues, or, if this is None, do not filter.
        :rtype: list
        :return: List of Session objects
        """
        raise NotImplementedError

    def get_venue(self, venue_name):
        """Returns Venue with ``venue_name``

        :type venue_name: str
        :rtype: models.Venue or None
        """
        raise NotImplementedError

    def get_venues(self):
        """Return all venues

        :returns: list of Venue models
        :rtype: list
        """
        raise NotImplementedError

    def get_employee(self, username):
        """Get Employee with ``username``

        :type username: str
        :rtype: models.Employee or None
        :returns: Employee model if exists otherwise, None
        """
        raise NotImplementedError

    def get_employee_shifts(self, username, start=None, end=None):
        """Return shifts for employee username

        :type username: str
        :type start: int
        :param start: Filter only shifts with a start_time greater
            than this (Unix Time), or, if this is None, do not filter.
        :type end: int
        :param end: Filter only shifts with an end_time smaller
            than this (Unix Time), or, if this is None, do not filter.
        :return: list of Shift models
        :rtype: list
        """
        raise NotImplementedError

    def get_sports(self):
        """Return list of all sports (as Sport models)

        :rtype: list
        :returns: A list like the following: [models.Sport(...), models.Sport(...)]
        """
        raise NotImplementedError

    def get_teams_for_session(self, session_id):
        """Return list of Team models for teams that are part of a session

        :type session_id: int
        :param session_id: ID of session for which to get teams for
        :rtype: list
        :returns: A list like the following: [models.Team(...), models.Team(...)]
        """
        raise NotImplementedError
