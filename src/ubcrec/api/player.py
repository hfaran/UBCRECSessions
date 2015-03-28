import re
from functools import partial

import bcrypt
from tornado_json.exceptions import api_assert
from tornado_json import schema

from ubcrec.handlers import APIHandler
from ubcrec.common import get_player, get_session, extend_sessions
from ubcrec.constants import USERTYPE_PLAYER, USERTYPE_EMPLOYEE
from ubcrec.web import authenticated
from ubcrec.models import Session


class Player(APIHandler):

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "full_name": {"type": "string"},
                "student_number": {"type": "number"},
                "password": {"type": "string"},
            },
            "required": ["full_name", "password", "student_number"],
        },
        output_schema={
            "type": "object",
            "properties": {
                "student_number": {"type": "number"}
            }
        }
    )
    def put(self):
        """
        PUT the required parameters to permanently register a new player

        * `full_name`: Full name of the student
        * `password`: Password for future logins
        * `student_number`: Student number of the player
        """
        # Get attributes from request body
        full_name = self.body['full_name']
        api_assert(
            re.match(r"^[A-z ]+$", full_name) is not None,
            400,
            "full_name may only contain letters and spaces."
        )
        password = self.body['password']
        student_number = self.body['student_number']

        # Check if a player with this name already exists
        existing_player = self.db_conn.get_player(student_number)
        api_assert(
            existing_player is None,
            409,
            log_message="{} is already registered.".format(student_number)
        )

        # Create a new user/write to DB
        salt = bcrypt.gensalt(rounds=12)
        self.db_conn.insert_player_data(
            name=full_name,
            student_number=student_number,
            password=bcrypt.hashpw(password.encode(),
                                   salt).decode(),
            salt=salt.decode()
        )

        # We also do the step of logging the player in after registration
        self.set_secure_cookie(
            "user",
            "{} {}".format(USERTYPE_PLAYER, student_number),
            self.settings['ubcrec'].session_timeout_days
        )

        return {"student_number": student_number}


class Me(APIHandler):

    @authenticated(USERTYPE_PLAYER)
    @schema.validate(
        output_schema={
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "student_number": {"type": "number"},
            }
        },
        output_example={
            "full_name": "John Smith",
            "student_number": 10235609
        }
    )
    def get(self):
        """
        (Player only) GET to retrieve player info
        """
        player = get_player(db_conn=self.db_conn,
                            student_number=self.get_current_user())
        return {
            "full_name": player.full_name,
            "student_number": player.student_number
        }


class Sessions(APIHandler):

    @authenticated(USERTYPE_PLAYER)
    @schema.validate(
        output_schema={
            "type": "array",
        },
    )
    def get(self):
        """
        (Player only) GET to retrieve session objects participated
        in/registered for
        """
        session_ids = self.db_conn.get_player_session_ids(
            self.get_current_user()
        )
        sessions = list(map(
            Session.to_dict,
            map(
                partial(get_session, self.db_conn),
                session_ids
            )
        ))
        extend_sessions(self.db_conn, sessions)
        return sessions


class StudentSessions(APIHandler):

    @authenticated(USERTYPE_EMPLOYEE)
    @schema.validate(
        output_schema={
            "type": "array",
        },
        output_example=[1, 56, 7859]
    )
    def get(self, student_number):
        """
        (Employees only) GET to retrieve IDs of sessions participated
        in/registered for by student with `student_number`
        """
        # Make sure student exists
        get_player(self.db_conn, student_number)

        session_ids = self.db_conn.get_player_session_ids(
            student_number
        )
        return session_ids
