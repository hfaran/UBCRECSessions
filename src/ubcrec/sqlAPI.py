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
        :type startShift: str
        :param startShift: Employees start shift
        :type endShift: str
        :param endShift: Employees end shift
        """
        self.cursor.execute(
            "INSERT INTO Working VALUES (? ,? ,?)",
            (Sin,
             startShift,
             endShift)
        )
        self.conn.commit()

    def insertVenueData(self, Name, Address):
        """
        :type Name: str
        :param Name: Venue name
        :type Address: str
        :param Address: Address of venue
        """
        self.cursor.execute(
            "INSERT INTO Venue VALUES (? ,?)", (Name, Address)
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

    def insertSessionData(self, startTime, endTime, sessionID, sportID,
                          venueName, results):
        """

        :type startTime: int
        :param startTime: Start time for a session in Unix Time (seconds)
        :type endTime: int
        :param endTime: End time for a session in Unix Time (seconds)s
        :type sessionID: int
        :param sessionID: ID for the drop-in session
        :type sportID: int
        :param sportID: ID for the sport type
        :type venueName: str
        :param venueName: Name of the venue
        :type results: str
        :param results: Result of the game (not sure)
        """
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

    def insertTeamParInData(self, teamName, teamID, numPlayers, sportID,
                            sessionID, venueName):
        """Inserting data for Team_ParticipatesIn table

        :type teamName: str
        :param teamName: Name of the team
        :type teamID: ID for team
        :param teamID: ID for team
        :type numPlayers: int
        :param numPlayers: Number of player in a team
        :type sportID: int
        :param sportID: ID for sport
        :type sessionID: int
        :param sessionID: ID for session
        :type venueName: str
        :param venueName: Name of the venue where the drop-in session is held
        """
        self.cursor.execute(
            "INSERT INTO Team_ParticipatesIn VALUES (?,?,?,?,?,?)",
            (teamName,
             teamID,
             numPlayers,
             sportID,
             sessionID,
             venueName)
        )
        self.conn.commit()

    def get_player(self, username):
        """Gets player with ``username``

        If no such player exists, return ``None``.

        :type username: str
        :param username: Username of player to find
        :returns: Model of player with user
        :rtype: models.Player or None
        """
        raise NotImplementedError

    def get_player_session_ids(self, username):
        """Returns list of IDs for session that player is/was registered in

        :type username: str
        :param username: Username of player to find
        :rtype: list
        :returns: list of session IDs
        """
        raise NotImplementedError
