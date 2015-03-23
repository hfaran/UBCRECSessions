import bcrypt

from tornado.web import authenticated
from tornado_json.exceptions import api_assert
from tornado_json import schema

from ubcrec.handlers import APIHandler


class Player(APIHandler):

    def post(self):
        """
        POST the required parameters to permanently register a new player

        * `username`: Username of the player
        * `password`: Password for future logins
        """
        username = self.body['username']
        password = self.body['password']

        raise NotImplementedError
        # TODO
