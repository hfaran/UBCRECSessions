from tornado_json import schema

from ubcrec.handlers import APIHandler
from ubcrec.common import get_session
from ubcrec import models


class Session(APIHandler):

    @schema.validate(
        output_schema={
            "type": "object",
            "properties": {
                "start_time": {"type": "number"},
                "end_time": {"type": "number"},
                "session_id": {"type": "number"},
                "sport_id": {"type": "number"},
                "venue_name": {"type": "string"},
                "results": {"type": "string"},
            }
        }
    )
    def get(self, session_id):
        """
        GET data for session with `session_id`
        """
        session = get_session(self.db_conn, session_id)
        return session.to_dict()


class Sessions(APIHandler):

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "started_after": {"type": "number"},
                "ended_before": {"type": "number"},
                "sports": {"type": "array"},
                "venues": {"type": "array"}
            }
        },
        output_schema={"type": "array"}
    )
    def get(self):
        """
        GET array of sessions matching given parameters

        * `started_after`: Filter only sessions with a start_time greater than this (Unix Time)
        * `end_before`: Filter only sessions with an end_time smaller than this (Unix Time)
        * `sports`: Array of sport names; filter only sessions for these sports
        * `venues`: Array of venue names; filter only sessions held in these venues
        """
        return list(map(
            models.Session.to_dict,
            self.db_conn.get_sessions(
                **{k: self.body.get(k, None) for k in [
                    "started_before",
                    "ended_before",
                    "sports",
                    "venues"
                ]}
            )
        ))
