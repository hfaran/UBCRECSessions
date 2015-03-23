from tornado_json import schema
from tornado_json.exceptions import api_assert, APIError

from ubcrec.handlers import APIHandler
from ubcrec.common import get_venue
from ubcrec.web import authenticated
from ubcrec import models
from ubcrec.constants import USERTYPE_EMPLOYEE


class Venue(APIHandler):

    @schema.validate(
        output_schema={
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "address": {"type": "string"}
            }
        }
    )
    def get(self, venue_name):
        """
        GET data for venue with ``venue_name``
        """
        venue = get_venue(self.db_conn, venue_name)
        return venue.to_dict()

    @authenticated(USERTYPE_EMPLOYEE)
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "address": {"type": "string"}
            }
        },
        output_schema={
            "type": "object",
            "properties": {
                "name": {"type": "string"}
            }
        }
    )
    def put(self):
        """
        PUT to add new venue
        """
        name = self.body['name']
        address = self.body['address']

        # Check to make sure venue doesn't already exist
        try:
            get_venue(self.db_conn, name)
        except APIError:
            pass
        else:
            raise APIError(
                409,
                log_message="Venue with name {} already exists.".format(name)
            )

        self.db_conn.create_venue(name=name, address=address)
        return {"name": name}


class Venues(APIHandler):

    @schema.validate(
        output_schema={"type": "array"}
    )
    def get(self):
        """
        GET all venues
        """
        return list(map(
            models.Venue.to_dict,
            self.db_conn.get_venues()
        ))
