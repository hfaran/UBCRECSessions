import re

import bcrypt
from tornado.web import authenticated
from tornado_json.exceptions import api_assert
from tornado_json import schema

from ubcrec.handlers import APIHandler
from ubcrec.common import get_player
from ubcrec.constants import USERTYPE_PLAYER


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
    def post(self):
        """
        POST the required parameters to permanently register a new player

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
            password=bcrypt.hashpw(str(password), salt),
            salt=salt
        )

        # We also do the step of logging the player in after registration
        self.set_secure_cookie(
            "user",
            "{} {}".format(USERTYPE_PLAYER, student_number),
            self.settings['ubcrec'].session_timeout_days
        )

        return {"student_number": student_number}


class Me(APIHandler):

    @authenticated
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
        GET to retrieve player info
        """
        player = get_player(db_conn=self.db_conn,
                            student_number=self.get_current_user())
        return {
            "full_name": player.full_name,
            "student_number": player.student_number
        }


class Sessions(APIHandler):

    @authenticated
    @schema.validate(
        output_schema={
            "type": "array",
        },
        output_example=[1, 56, 7859]
    )
    def get(self):
        """
        GET to retrieve IDs of sessions participated in/registered for
        """
        session_ids = self.db_conn.get_player_session_ids(
            self.get_current_user()
        )
        return session_ids
