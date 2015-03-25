from tornado_json import schema

from ubcrec.handlers import APIHandler
from ubcrec.common import get_session
from ubcrec.web import authenticated
from ubcrec import models
from ubcrec.constants import USERTYPE_EMPLOYEE


class Teams(APIHandler):

    @schema.validate(
        output_schema={"type": "array"},
        output_example=[{
            "team_id": 1,
            "name": "The Team",
            "num_max_players": 8,
            "session_id": 5
        }]
    )
    def get(self, session_id):
        """
        GET array of all teams for the given `session_id`
        """
        # Make sure such a session exists
        get_session(self.db_conn, session_id)

        return list(map(
            models.Team.to_dict,
            self.db_conn.get_teams_for_session(int(session_id))
        ))


class Team(APIHandler):

    @authenticated(USERTYPE_EMPLOYEE)
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "num_max_players": {"type": "number"},
                "session_id": {"type": "number"},
            }
        },
        output_schema={
            "type": "object",
            "properties": {
                "team_id": {"type": "number"}
            }
        }
    )
    def put(self):
        """
        (Employees Only) Create a team for a session

        * `name`: Name of team
        * `num_max_players`: Maximum number of players that can join this team
        * `session_id`: ID of session which this team is for
        """
        session_id = self.body['session_id']
        num_max_players = self.body['num_max_players']
        name = self.body['name']

        # Make sure such a session exists
        get_session(self.db_conn, session_id)

        team_id = self.db_conn.create_team(
            name=name,
            num_max_players=num_max_players,
            session_id=session_id
        )

        return dict(team_id=team_id)
