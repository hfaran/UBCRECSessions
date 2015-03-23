from tornado_json.exceptions import api_assert

from ubcrec.models import Player, Session, Venue, Employee


def get_player(db_conn, student_number):
    """Get player with ``student_number``

    :type student_number: int or str
    :rtype: Player or None
    """
    player = db_conn.get_player(int(student_number))

    api_assert(
        player is not None,
        409,
        log_message="No player with student number {} exists.".format(
            student_number
        )
    )

    return player


def get_session(db_conn, session_id):
    """Get player with ``session_id``

    :type session_id: int or str
    :rtype: Session or None
    """
    session = db_conn.get_session(int(session_id))

    api_assert(
        session is not None,
        409,
        log_message="No session with ID {} exists.".format(session_id)
    )

    return session


def get_venue(db_conn, venue_name):
    """Get Venue with ``venue_name``

    :type venue_name: str
    :rtype: Venue or None
    """
    venue = db_conn.get_venue(venue_name)

    api_assert(
        venue is not None,
        409,
        log_message="No Venue with name {} exists.".format(venue_name)
    )

    return venue


def get_employee(db_conn, username):
    """Get Employee with ``username``

    :type username: str
    :rtype: Employee or None
    """
    employee = db_conn.get_employee(username)

    api_assert(
        employee is not None,
        409,
        log_message="No Employee with username {} exists.".format(username)
    )

    return employee
