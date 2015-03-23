from tornado_json.exceptions import api_assert

from ubcrec.models import Player, Session


def get_player(db_conn, student_number):
    """Get player with ``student_number``

    :rtype: Player or None
    """
    player = db_conn.get_player(student_number)

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

    :rtype: Session or None
    """
    session = db_conn.get_session(session_id)

    api_assert(
        session is not None,
        409,
        log_message="No session with ID {} exists.".format(session_id)
    )

    return session
