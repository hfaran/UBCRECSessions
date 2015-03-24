from tornado_json import schema

from ubcrec.handlers import APIHandler
from ubcrec.web import authenticated
from ubcrec import models
from ubcrec.constants import USERTYPE_EMPLOYEE


class Schedule(APIHandler):

    @authenticated(USERTYPE_EMPLOYEE)
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "start": {"type": "number"},
                "end": {"type": "number"},
            }
        },
        output_schema={"type": "array"}
    )
    def get(self):
        """
        GET employee shifts from `start` to `end`

        * `start`: Only shifts with a start_time greater than start will be
            returned
        * `end`: Only shifts with a end_time smaller than end will be
            returned
        """
        return list(map(
            models.Shift.to_dict,
            self.db_conn.get_employee_shifts(
                start=self.body.get("start", None),
                end=self.body.get("end", None),
                username=self.get_current_user()
            )
        ))
