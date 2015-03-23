import sqlite3


class SQLAPI(object):
    """Abstraction for database

    :type db_path: str
    :param db_path: String containing address of the database
    """
    def __init__(self, db_path='project.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def tableCreate(self):
        """
        :rtype : object
        Note: This function is creates the tables and stuff but does not properly set the foreign and primary keys.
        We only need to do this one and therefore we can do it using SQL manager once and use it for the rest of time
        So use this for testing only.
        """
        self.cursor.execute("CREATE TABLE Employees (sin TEXT, fName TEXT, lName TEXT, username TEXT,password TEXT,salt TEXT)")
        self.cursor.execute("CREATE TABLE Working  (sin TEXT, startShift TEXT, endShift TEXT)")
        self.cursor.execute("CREATE TABLE Venue   (name TEXT, address TEXT)")
        self.cursor.execute("CREATE TABLE Sport (name TEXT, sportID INT)")
        # Note that I am using the start and end time as string. we initially had it as int.
        self.cursor.execute("CREATE TABLE Session  (start_time TEXT, end_time TEXT, session_id UNSIGNED INT, sport_id UNSIGNED INT, venue_name TEXT, results TEXT)")
        self.cursor.execute("CREATE TABLE Player (name TEXT , student_num UNSIGNED INT, password TEXT, salt TEXT)")
        self.cursor.execute("CREATE TABLE PlaysIn (student_num UNSIGNED INT, team_id UNSIGNED INT)")
        self.cursor.execute("CREATE TABLE Team_ParticipatesIn (name TEXT, team_ID UNSIGNED INT, number_of_players UNSIGNED INT,"
                       "sport_id UNSIGNED INT, session_id INT,venue_name TEXT)")

    # Below are the functions used to update each table of the database for the schemas we defined.
    # Function names and attributes are self-explanatory.

    def insertEmployeesData(self,Sin,fName, lName,username, password,salt ):
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
        :raise TypeError: if the above type doesnt match it will throw an exception
        """
        if (isinstance(Sin,str)==True and isinstance(fName,str)==True and isinstance(lName,str)==True
            and isinstance(username,str)==True and isinstance(password,str)==True and isinstance(salt,str)==True):
            self.cursor.execute("INSERT INTO Employees VALUES (? ,? ,? ,? ,? ,?)",(Sin,fName,lName,username,password,salt))
            self.conn.commit()
        else:
            raise TypeError("Element type is not valid.")
            #print("Insertion for Employee table failed. Types doesn't match.")

    def insertWorkingData(self,Sin,start_shift, end_shift ):
        """
        :type Sin: str
        :param Sin: Employees SIN number
        :type start_shift: str
        :param start_shift: Employees start shift
        :type end_shift: str
        :param end_shift: Employees end shift
        """
        if (isinstance(Sin,str)==True and isinstance(start_shift,str)==True and isinstance(end_shift,str)==True):
            self.cursor.execute("INSERT INTO Working VALUES (? ,? ,?)",Sin,start_shift,end_shift)
            self.conn.commit()
        else:
            raise TypeError("Element type is not valid.")
            #print("Insertion for Working table failed. Types doesn't match.")

    def insertVenueData(self,Name,Address):
        """
        :type Name: str
        :param Name: Venue name
        :type Address: str
        :param Address: Address of venue
        """
        if (isinstance(Name,str)==False) :
            raise TypeError("Name type must be string.")
            #print("Inserting Name for Venue table failed. Types doesn't match.")
        elif (isinstance(Address,str)==False ):
            raise TypeError("Address type must be string.")
            #print("Inserting Address for Venue table failed. Types doesn't match.")
        else:
            self.cursor.execute("INSERT INTO Venue VALUES (? ,?)",(Name,Address))
            self.conn.commit()

    def insertSportData (self, sportName, sportID):
        """

        :type sportName: str
        :param sportName: Name of the sport
        :type sportID: int
        :param sportID: ID of the sport type
        """
        if (isinstance(sportName,str)==False):
            raise TypeError("sportName type must be string.")
            #print("Inserting Sport Name for Sport table failed. Type doesn't match.")
        elif (isinstance(sportID,int)==False or sportID<0):
            raise TypeError("sportID type must be integer.")
            #cprint("Inserting Sport ID for Sport table failed. Type doesn't match.")
        else:
            self.cursor.execute("INSERT INTO Sport VALUES (? ,?)",(sportName,sportID))
            self.conn.commit()

    def insertSessionData (self, startTime, endTime, sessionID, sportID,venueName,results):
        """

        :type startTime: str
        :param startTime: Start time for a session. The time when session starts
        :type endTime: str
        :param endTime: End time for a session. The time when session ends
        :type sessionID: int
        :param sessionID: ID for the drop-in session
        :type sportID: int
        :param sportID: ID for the sport type
        :type venueName: str
        :param venueName: Name of the venue
        :type results: str
        :param results: Result of the game (not sure)
        """
        """Note: we had start time and end time as int but i am using it as string here"""
        if (isinstance(startTime,str)==True and isinstance(endTime,str)==True and isinstance(sessionID,int)==True
        and isinstance(sportID,int) and sportID>=0 and isinstance(venueName,str)==True and isinstance(results,str)):
            self.cursor.execute("INSERT INTO Session VALUES (? ,?,? ,?,? ,?)",(startTime,endTime,sessionID,sportID,venueName,results))
            self.conn.commit()
        else:
            raise TypeError("Element type is not valid.")
            #print("Insertion for Session table failed. Types doesn't match.")

    def insertPlayerData (self, name, studentID, password, salt):
        """
        :type name: str
        :param name: Name of the student/player
        :type studentID:int
        :param studentID: Student ID of the player
        :type password: str
        :param password: Password for that student
        :type salt: str
        :param salt: I dont know
        """
        if (isinstance(name,str)==True and isinstance(password,str)==True
        and isinstance(studentID,int) and studentID>=0 and isinstance(salt,str)==True ):
            self.cursor.execute("INSERT INTO Player VALUES (?,?,?,?)",(name,password,studentID,salt))
            self.conn.commit()
        else:
            raise TypeError("Element type is not valid.")
            #print("Insertion for Player table failed. Types doesn't match.")

    def insertPlaysInData (self, studentNum, teamID):
        """
        :type studentNum int
        :param studentNum: Student number of the player
        :type teamID: int
        :param teamID: Team ID
        """
        if (isinstance(studentNum,str)==False):
            raise TypeError("Student number  type must be string.")
            #print("Inserting student Number for PlaysIn table failed. Type doesn't match.")
        elif (isinstance(teamID,int)==False or teamID<0):
            raise TypeError("Team ID is either not string or its value is negative.")
            #print("Inserting team ID for PlaysIn table failed. Type doesn't match.")
        else:
            self.cursor.execute("INSERT INTO PlaysIn VALUES (? ,?)",(studentNum,teamID))
            self.conn.commit()

    def insertTeamParInData(self,teamName,teamID,numPlayers,sportID,sessionID,venueName):
        """

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
        """Inserting data for Team_ParticipatesIn table """
        if (isinstance(teamName,str)==True and isinstance(teamID,int)==True and teamID>=0
            and isinstance(sessionID,int)==True and isinstance(sportID,int) and sportID>=0
            and isinstance(venueName,str)==True and isinstance(numPlayers,int) and numPlayers>0):
            self.cursor.execute("INSERT INTO TeamParIn VALUES (?,?,?,?,?,?)",(teamName,teamID,numPlayers,sportID,sessionID,venueName))
            self.conn.commit()
        else:
            raise TypeError("Element type is not valid.")
            #print("Insertion for Team_ParticipatesIn table failed. Types doesn't match.")
