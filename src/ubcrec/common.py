from tornado_json.exceptions import api_assert

from ubcrec.models import Player


def get_player(db_conn, username):
    """Get player with ``username``

    :rtype: Player or None
    """
    player = db_conn.get_player(username)

    api_assert(
        player is not None,
        409,
        log_message="No player {} exists.".format(username)
    )

    return player
