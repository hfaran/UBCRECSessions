__author__ = 'Ehsan'
import sqlite3

class sqlAPI:

    """
    Note: This function is creates the tables and stuff but does not properly set the foreign and primary keys.
    We only need to do this one and therefore we can do it using SQL manager once and use it for the rest of time
    So use this for testing only.
    """
    def tableCreate(self):
        self.c.execute("CREATE TABLE Employees (sin TEXT, fName TEXT, lName TEXT, username TEXT,password TEXT,salt TEXT)")
        self.c.execute("CREATE TABLE Working  (sin TEXT, startShift TEXT, endShift TEXT)")
        self.c.execute("CREATE TABLE Venue   (name TEXT, address TEXT)")
        self.c.execute("CREATE TABLE Sport (name TEXT, sportID INT)")
        """ Note that I am using the start and end time as string. we initially had it as int."""
        self.c.execute("CREATE TABLE Session  (start_time TEXT, end_time TEXT, session_id UNSIGNED INT, sport_id UNSIGNED INT, venue_name TEXT, results TEXT)")
        self.c.execute("CREATE TABLE Player (name TEXT , student_num UNSIGNED INT, password TEXT, salt TEXT)")
        self.c.execute("CREATE TABLE PlaysIn (student_num UNSIGNED INT, team_id UNSIGNED INT)")
        self.c.execute("CREATE TABLE Team_ParticipatesIn (name TEXT, team_ID UNSIGNED INT, number_of_players UNSIGNED INT,"
                       "sport_id UNSIGNED INT, session_id INT,venue_name TEXT)")


    """
    input : String containing address of the database
    output: the cursor for that database for later use
    """
    def setUp(self, DBaddress='project.db'):
        if isinstance(DBaddress,str):
            self.conn = sqlite3.connect(DBaddress)
            self.c = self.conn.cursor()
            return self.c
        else :
            print ("Address of the database is not string/valid")

    """
    Below are the functions used to update each table of the database for the schemas we defined.
    Function names and attributes are self-explanatory.
    """
    def insertEmployeesData(self,Sin,fName, lName,username, password,salt ):
        if (isinstance(Sin,str)==True and isinstance(fName,str)==True and isinstance(lName,str)==True
            and isinstance(username,str)==True and isinstance(password,str)==True and isinstance(salt,str)==True):
            self.c.execute("INSERT INTO Employees VALUES (? ,? ,? ,? ,? ,?)",(Sin,fName,lName,username,password,salt))
            self.conn.commit()
        else:
            print("Insertion for Employee table failed. Types doesn't match.")

    def insertWorkingData(self,Sin,start_shift, end_shift ):
        if (isinstance(Sin,str)==True and isinstance(start_shift,str)==True and isinstance(end_shift,str)==True):
            self.c.execute("INSERT INTO Working VALUES (? ,? ,?)",Sin,start_shift,end_shift)
            self.conn.commit()
        else:
            print("Insertion for Working table failed. Types doesn't match.")

    def insertVenueData(self,Name,Address):
        if (isinstance(Name,str)==False) :
            print("Inserting Name for Venue table failed. Types doesn't match.")
        elif (isinstance(Address,str)==False ):
            print("Inserting Address for Venue table failed. Types doesn't match.")
        else:
            self.c.execute("INSERT INTO Venue VALUES (? ,?)",(Name,Address))
            self.conn.commit()

    def insertSportData (self, sportName, sportID):
        if (isinstance(sportName,str)==False):
            print("Inserting Sport Name for Sport table failed. Type doesn't match.")
        elif (isinstance(sportID,int)==False or sportID<0):
            print("Inserting Sport ID for Sport table failed. Type doesn't match.")
        else:
            self.c.execute("INSERT INTO Sport VALUES (? ,?)",(sportName,sportID))
            self.conn.commit()

    """Note: we had start time and end time as int but i am using it as string here"""
    def insertSessionData (self, startTime, endTime, sessionID, sportID,venueName,results):
        if (isinstance(startTime,str)==True and isinstance(endTime,str)==True and isinstance(sessionID,int)==True
        and isinstance(sportID,int) and sportID>=0 and isinstance(venueName,str)==True and isinstance(results,str)):
            self.c.execute("INSERT INTO Session VALUES (? ,?,? ,?,? ,?)",(startTime,endTime,sessionID,sportID,venueName,results))
            self.conn.commit()
        else:
            print("Insertion for Session table failed. Types doesn't match.")

    def insertPlayerData (self, name, studentID, password, salt):
        if (isinstance(name,str)==True and isinstance(password,str)==True
        and isinstance(studentID,int) and studentID>=0 and isinstance(salt,str)==True ):
            self.c.execute("INSERT INTO Player VALUES (?,?,?,?)",(name,password,studentID,salt))
            self.conn.commit()
        else:
            print("Insertion for Player table failed. Types doesn't match.")


    def insertPlaysInData (self, studentNum, teamID):
        if (isinstance(studentNum,str)==False):
            print("Inserting student Number for PlaysIn table failed. Type doesn't match.")
        elif (isinstance(teamID,int)==False or teamID<0):
            print("Inserting team ID for PlaysIn table failed. Type doesn't match.")
        else:
            self.c.execute("INSERT INTO PlaysIn VALUES (? ,?)",(studentNum,teamID))
            self.conn.commit()

    """Inserting data for Team_ParticipatesIn table """
    def insertTeamParInData(self,teamName,teamID,numPlayers,sportID,sessionID,venueName):
        if (isinstance(teamName,str)==True and isinstance(teamID,int)==True and teamID>=0
            and isinstance(sessionID,int)==True and isinstance(sportID,int) and sportID>=0
            and isinstance(venueName,str)==True and isinstance(numPlayers,int) and numPlayers>0):
            self.c.execute("INSERT INTO TeamParIn VALUES (?,?,?,?,?,?)",(teamName,teamID,numPlayers,sportID,sessionID,venueName))
            self.conn.commit()
        else:
            print("Insertion for Team_ParticipatesIn table failed. Types doesn't match.")