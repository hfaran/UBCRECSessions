import bcrypt

from tornado.web import authenticated
from tornado_json.exceptions import api_assert
from tornado_json import schema

from ubcrec.handlers import APIHandler
from ubcrec.common import get_player


class Player(APIHandler):

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "student_number": {"type": "number"},
                "password": {"type": "string"},
            },
            "required": ["username", "password", "student_number"],
        },
        output_schema={
            "type": "object",
            "properties": {
                "username": {"type": "string"}
            }
        }
    )
    def post(self):
        """
        POST the required parameters to permanently register a new player

        * `username`: Username of the player
        * `password`: Password for future logins
        * `student_number`: Student number of the player
        """
        # Get attributes from request body
        username = self.body['username']
        password = self.body['password']
        student_number = self.body['student_number']

        # Check if a player with this name already exists
        existing_player = self.db_conn.get_player(username)
        api_assert(
            existing_player is None,
            409,
            log_message="{} is already registered.".format(username)
        )

        # Create a new user/write to DB
        salt = bcrypt.gensalt(rounds=12)
        self.db_conn.insert_player_data(
            name=username,
            student_number=student_number,
            password=bcrypt.hashpw(str(password), salt),
            salt=salt
        )

        # We also do the step of logging the player in after registration
        self.set_secure_cookie(
            "user",
            username,
            self.settings['ubcrec'].session_timeout_days
        )

        return {"username": username}


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
            "username": "john_smith",
            "student_number": 10235609
        }
    )
    def get(self):
        """
        GET to retrieve player info
        """
        player = get_player(db_conn=self.db_conn,
                            username=self.get_current_user())
        return {
            "username": player.username,
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
