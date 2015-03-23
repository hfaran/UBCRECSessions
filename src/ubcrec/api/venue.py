from tornado_json import schema

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
