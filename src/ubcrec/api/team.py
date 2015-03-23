from tornado_json import schema
from tornado_json.exceptions import api_assert

from ubcrec.handlers import APIHandler
from ubcrec.common import get_session, get_team
from ubcrec.web import authenticated
from ubcrec import models
from ubcrec.constants import USERTYPE_EMPLOYEE, USERTYPE_PLAYER


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


class Register(APIHandler):

    @authenticated(USERTYPE_PLAYER)
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "team_id": {"type": "number"}
            }
        },
        output_schema={
            "type": "object",
            "properties": {
                "team_id": {"type": "number"}
            }
        }
    )
    def post(self):
        """
        (Student only) POST to register self in Team with given `team_id`

        * `team_id`: ID of team to register in
        """
        team_id = self.body['team_id']

        # Test if team exists/get existing team
        team = get_team(self.db_conn, team_id=team_id)

        # Only add player to team if there is room
        api_assert(
            team.num_max_players > self.db_conn.get_num_players_registered(
                int(team_id)
            ),
            409,
            log_message=("Team {name} (ID {id}) is full! Cannot add you "
                         "to team.".format(name=team.name, id=team_id))
        )

        # All seems good at this point so register player in team
        self.db_conn.register_player_in_team(
            student_num=int(self.get_current_user()),
            team_id=int(team_id)
        )

        return dict(team_id=team_id)
