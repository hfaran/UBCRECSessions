import sqlite3

# not sure about the below
import models


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

    # TODO: change this to insert_venue
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

        # TODO whay is this create ? lool need to change that to insert_session -> let Hamza know
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

    def register_player_in_team(self, student_num, team_id):
        """
        :type student_num int
        :param student_num: Student number of the player
        :type team_id: int
        :param team_id: Team ID
        """
        self.cursor.execute(
            "INSERT INTO PlaysIn (student_num, team_id) VALUES (? ,?)",
            (student_num, team_id)
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
        self.cursor.execute('SELECT * FROM Player WHERE student_num=?', (student_number,))
        row = self.cursor.fetchall()

        # I am adding this in case I messed up during the database setup
        if (len(row) > 1):
            raise (IndexError, "There is something wrong with the primary key of Player Table. Duplicated keys")
        elif (len(row) == 1):
            # schema: Player (name: string , student_num: uint, password: string, salt: string)
            player_model = models.Player(row[0],row[1],row[2],row[3])
            return player_model
        else :
            return None

    def get_player_session_ids(self, student_number):
        """Returns list of IDs for session that player is/was registered in

        :type student_number: int
        :param student_number: Student number of player to find
        :rtype: list
        :returns: list of session IDs
        """
        self.cursor.execute('SELECT session_id FROM Session WHERE student_num=?', (student_number,))
        row = self.cursor.fetchall()

        return row

    def get_session(self, session_id):
        """Returns session with ``session_id``

        :type session_id: int
        :param session_id: ID of session
        :return: Session or None if no such session with ``session_id`` exists
        :rtype: models.Session or None
        """
        self.cursor.execute('SELECT * FROM Session WHERE session_id=?', (session_id,))
        row = self.cursor.fetchall()
        # I am adding this in case I messed up during the database setup
        if (len(row) > 1):
            raise (IndexError, "There is something wrong with the primary key of Session Table. Duplicated keys")
        elif (len(row) == 1):
            # Session (start_time: integer, end_time: integer, session_id: integer, sport_id: uint, venue_name: string, results: string)
            session_model = models.Session(row[0],row[1],row[2],row[3],row[4],row[5])
            return session_model
        else:
            return None

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
        self.cursor.execute('SELECT * FROM Venue WHERE venue_name=?', (venue_name,))
        row = self.cursor.fetchall()
        # I am adding this in case I messed up during the database setup
        if (len(row) > 1):
            raise (IndexError, "There is something wrong with the primary key of Session Table. Duplicated keys")
        elif (len(row) == 1):
            venue_model = models.Venue(row[0],row[1])
            return venue_model
        else:
            return None

    def get_venues(self):
        """Return all venues

        :returns: list of Venue models
        :rtype: list
        """
        self.cursor.execute('SELECT * FROM Venue')
        row = self.cursor.fetchall()
        if (len(row) > 0):
            return row
        else:
            return None

    def get_employee(self, username):
        """Get Employee with ``username``

        :type username: str
        :rtype: models.Employee or None
        :returns: Employee model if exists otherwise, None
        """
        self.cursor.execute('SELECT * FROM Employees WHERE venue_name=?', (username,))
        row = self.cursor.fetchall()
        # I am adding this in case I messed up during the database setup
        if (len(row) > 1):
            raise (IndexError, "There is something wrong with the primary key of Employees Table. Duplicated keys")
        elif (len(row) == 1):
            employee_model = models.Employee(row[0],row[1],row[2],row[3],row[4],row[5])
            return employee_model
        else:
            return None

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

        # I dont understand what you need from this function, need to discuss
        # TODO: discuss the fucntionality
        if start==None:
            print "Check start conditions"
            # raise MyBrainDoesntWork
            # get the sin for the username
            #use the sin in Working table and check if start_time greater than start
        elif end==None:
            print "Check end conditions"
            # get the sin for the username (cause Working schema has sin)
            #use the sin in Working table and check if start_time greater than start
        else:
            print "Check both start and end condition"
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

    def get_team(self, team_id):
        """Return Team model with ``team_id``

        :type team_id: int
        :rtype: models.Team or None
        :returns: Team model or None if doesn't exist
        """
        raise NotImplementedError

    def get_num_players_registered(self, team_id):
        """Return count of players CURRENTLY registered (i.e., PlaysIn) in
        ``team_id``.

        You can assume that a team with ``team_id`` definitely exists.

        :type team_id: int
        :rtype: int
        """
        raise NotImplementedError
