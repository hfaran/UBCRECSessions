import bcrypt

from tornado.web import authenticated
from tornado.options import options
from tornado_json.exceptions import api_assert
from tornado_json import schema

from ubcrec.handlers import APIHandler


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
            options.session_timeout_days
        )

        return {"username": username}

    @authenticated
    @schema.validate(
        output_schema={
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "student_number": {"type": "number"},
            }
        },
    )
    def get(self):
        """
        GET to retrieve player info
        """
        username = self.get_current_user()
        player = self.db_conn.get_player(username)

        api_assert(
            player is not None,
            409,
            log_message="No user {} exists.".format(username)
        )

        return {
            "username": player.username,
            "student_number": player.student_number
        }
