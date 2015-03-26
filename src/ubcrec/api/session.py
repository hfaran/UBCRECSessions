from tornado_json import schema

from ubcrec.handlers import APIHandler
from ubcrec.common import get_session
from ubcrec.web import authenticated
from ubcrec import models
from ubcrec.constants import USERTYPE_EMPLOYEE


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

    @authenticated(USERTYPE_EMPLOYEE)
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "start_time": {"type": "number"},
                "end_time": {"type": "number"},
                "sport_id": {"type": "number"},
                "venue_name": {"type": "string"},
            },
            "required": ["start_time", "end_time", "sport_id", "venue_name"]
        },
        output_schema={
            "type": "object",
            "properties": {
                "session_id": {"type": "number"}
            }
        }
    )
    def put(self):
        """
        PUT to create a new session

        * `start_time`: Time session starts in Unix Time
        * `end_time`: Time session ends in Unix Time
        * `sport_id`: ID of sport this session is for
        * `venue_name`: Name of venue where this session is held
        """
        start_time = self.body['start_time']
        end_time = self.body['end_time']
        sport_id = self.body['sport_id']
        venue_name = self.body['venue_name']

        session_id = self.db_conn.create_session(
            startTime=start_time,
            endTime=end_time,
            sportID=sport_id,
            venueName=venue_name
        )

        return {"session_id": session_id}

    @authenticated(USERTYPE_EMPLOYEE)
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "session_id": {"type": "number"},
                "results": {"type": "string"}
            },
            "required": ["session_id", "results"]
        },
        output_schema={
            "type": "object",
            "properties": {
                "session_id": {"type": "number"},
            }
        }
    )
    def patch(self):
        """
        PATCH to add/amend results for a session

        * `results`: String noting results of a session
        """
        session_id = self.body['session_id']
        results = self.body['results']

        # Make sure session exists
        get_session(self.db_conn, session_id)

        self.db_conn.add_session_results(session_id, results)

        return {"session_id": session_id}

    @authenticated(USERTYPE_EMPLOYEE)
    @schema.validate()
    def delete(self, session_id):
        """
        (Employees Only) DELETE session with `session_id`
            (cascade through teams for that session)
        """
        # Make sure session exists
        get_session(self.db_conn, session_id=session_id)

        self.db_conn.delete_session(int(session_id))


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
    def post(self):
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
