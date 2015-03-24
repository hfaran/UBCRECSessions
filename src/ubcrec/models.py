class Player(object):
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


class Employee(object):
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


class Session(object):
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


class Venue(object):
    """Venue Model

    :type name: str
    :type address: str
    """
    def __init__(self, name, address):
        self.name = name
        self.address = address
