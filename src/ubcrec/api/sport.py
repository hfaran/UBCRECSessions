from tornado_json import schema

from ubcrec.handlers import APIHandler
from ubcrec import models


class Sports(APIHandler):

    @schema.validate(
        output_schema={
            "type": "array",
        },
        output_example=[
            {
                "sport_id": 1,
                "name": "Basketball"
            },
            {
                "sport_id": 2,
                "name": "Futsal"
            }
        ]
    )
    def get(self):
        """
        GET array of all sports
        """
        return list(map(
            models.Sport.to_dict,
            self.db_conn.get_sports()
        ))
