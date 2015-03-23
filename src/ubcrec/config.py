class UBCRECConfig(object):
    """Class containing configuration/settings for the application

    :type port: int
    :param port: Port to start server on
    :type db_file: str
    :param db_file: Path of database file
    :type session_timeout_days: float or None
    :param session_timeout_days: Cookie expiration time in days; can also be
        set to ``None`` for session cookies, i.e., cookies that expire when
        browser window is closed.
    :type cookie_secret: str
    :param cookie_secret: Set this to an empty string to generate a new
        cookie secret each time the server is restarted, or to any string
        which is the cookie secret.
    """
    def __init__(self, port, db_file, session_timeout_days, cookie_secret):
        self.port = port
        self.db_file = db_file
        self.session_timeout_days = session_timeout_days
        self.cookie_secret = cookie_secret
