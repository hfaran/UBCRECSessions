import json


class Model(object):

    def to_dict(self):
        raise NotImplementedError

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)


class Player(Model):
    """Model of Player

    :type student_number: int
    :type full_name: str
    :type hashed_pass: str
    :type salt: str
    """
    def __init__(self, student_number, full_name, hashed_pass, salt):
        self.student_number = student_number
        self.full_name = full_name
        self.hashed_pass = hashed_pass
        self.salt = salt


class Employee(Model):
    """Employee Model

    :type sin: int
    :type first_name: str
    :type last_name: str

    :type username: str
    :type hashed_pass: str
    :type salt: str
    """
    def __init__(self, sin, first_name, last_name, username, hashed_pass, salt):
        self.sin = sin
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.hashed_pass = hashed_pass
        self.salt = salt


class Session(Model):
    """"Session Model

    :type start_time: int
    :type end_time: int
    :type session_id: int
    :type sport_id: int
    :type venue_name: str
    :type results: str
    """
    def __init__(self, start_time, end_time, session_id, sport_id, venue_name,
               results):
        self.start_time = start_time
        self.end_time = end_time
        self.session_id = session_id
        self.sport_id = sport_id
        self.venue_name = venue_name
        self.results = results

    def to_dict(self):
        return {k: getattr(self, k) for k in [
            "start_time",
            "end_time",
            "session_id",
            "sport_id",
            "venue_name",
            "results"
        ]}


class Venue(Model):
    """Venue Model

    :type name: str
    :type address: str
    """
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_dict(self):
        return {k: getattr(self, k) for k in [
            "name",
            "address",
        ]}


class Shift(Model):
    """Shift (for employees) model

    :type username: str
    :type start_time: int
    :type end_time: int
    """
    def __init__(self, username, start_time, end_time):
        self.username = username
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {k: getattr(self, k) for k in [
            "username",
            "start_time",
            "end_time"
        ]}


class Sport(Model):
    """Sport model

    :type sport_id: int
    :type name: str
    """
    def __init__(self, sport_id, name):
        self.sport_id = sport_id
        self.name = name

    def to_dict(self):
        return {k: getattr(self, k) for k in [
            "sport_id",
            "name",
        ]}


class Team(Model):
    """Team model

    :type team_id: int
    :type name: str
    :type num_max_players: int
    :type session_id: int
    """
    def __init__(self, team_id, name, num_max_players, session_id):
        self.team_id = team_id
        self.name = name
        self.num_max_players = num_max_players
        self.session_id = session_id

    def to_dict(self):
        return {k: getattr(self, k) for k in [
            "team_id",
            "name",
            "num_max_players",
            "session_id"
        ]}
