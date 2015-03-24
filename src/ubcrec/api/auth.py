import bcrypt
from tornado_json import schema
from tornado_json.exceptions import APIError

from ubcrec.web import authenticated
from ubcrec.handlers import APIHandler
from ubcrec.common import get_player
from ubcrec.constants import USERTYPE_PLAYER, USERTYPE_EMPLOYEE


class PlayerLogin(APIHandler):

    @schema.validate(
        input_schema={
            "required": ["student_number", "password"],
            "type": "object",
            "properties": {
                "student_number": {"type": "string"},
                "password": {"type": "string"},
            },
        },
        output_schema={
            "type": "object",
            "properties": {
                "student_number": {"type": "string"}
            }
        },
    )
    def post(self):
        """
        POST the required credentials to get back a cookie

        * `student_number`: Student Number
        * `password`: Password
        """
        student_number = self.body['student_number']
        password = self.body['password']
        player = get_player(self.db_conn, self.get_current_user())

        # Check if the given password hashed with the player's known
        #   salt matches the stored password
        password_match = bcrypt.hashpw(
            str(password), str(player.salt)
        ) == player.hashed_pass
        if password_match:
            self.set_secure_cookie(
                "user",
                "{} {}".format(USERTYPE_PLAYER, student_number),
                self.settings['ubcrec'].session_timeout_days
            )
            return {"student_number": student_number}
        else:
            raise APIError(
                400,
                log_message="Bad student_number/password combo"
            )

    @schema.validate(
        output_schema={"type": "string"}
    )
    def get(self):
        """GET to check if authenticated.

        Should be obvious from status code (403 vs. 200).
        """
        if not self.get_current_user():
            raise APIError(
                403,
                log_message="Please post to {} to get a cookie".format(
                    "/api/auth/playerlogin")
            )
        else:
            return "You are already logged in."


class Logout(APIHandler):
    """Logout"""

    @authenticated([USERTYPE_PLAYER, USERTYPE_EMPLOYEE])
    @schema.validate(
        output_schema={"type": "string"},
    )
    def delete(self):
        """DELETE to clear cookie for current user."""
        self.clear_cookie("user")
        return "Logout was successful."
