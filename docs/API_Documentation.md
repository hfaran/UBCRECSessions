**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/auth/employeelogin/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "password": {
            "type": "string"
        },
        "username": {
            "type": "string"
        }
    },
    "required": [
        "username",
        "password"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "username": {
            "type": "string"
        }
    },
    "type": "object"
}
```



**Notes**

POST the required credentials to get back a cookie

* `username`: Username
* `password`: Password



## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "string"
}
```



**Notes**

GET to check if authenticated.

Should be obvious from status code (403 vs. 200).



<br>
<br>

# /api/auth/logout/?

    Content-Type: application/json

## DELETE


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "string"
}
```



**Notes**

DELETE to clear cookie for current user.



<br>
<br>

# /api/auth/playerlogin/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "password": {
            "type": "string"
        },
        "student_number": {
            "type": "number"
        }
    },
    "required": [
        "student_number",
        "password"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "student_number": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Notes**

POST the required credentials to get back a cookie

* `student_number`: Student Number
* `password`: Password



## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "string"
}
```



**Notes**

GET to check if authenticated.

Should be obvious from status code (403 vs. 200).



<br>
<br>

# /api/employee/schedule/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "end": {
            "type": "number"
        },
        "start": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Output Schema**
```json
{
    "type": "array"
}
```



**Notes**

GET employee shifts from `start` to `end`

* `start`: Only shifts with a start_time greater than start will be
    returned
* `end`: Only shifts with a end_time smaller than end will be
    returned



<br>
<br>

# /api/player/me/?

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "properties": {
        "student_number": {
            "type": "number"
        },
        "username": {
            "type": "string"
        }
    },
    "type": "object"
}
```


**Output Example**
```json
{
    "full_name": "John Smith",
    "student_number": 10235609
}
```


**Notes**

(Player only) GET to retrieve player info



<br>
<br>

# /api/player/player/?

    Content-Type: application/json

## PUT


**Input Schema**
```json
{
    "properties": {
        "full_name": {
            "type": "string"
        },
        "password": {
            "type": "string"
        },
        "student_number": {
            "type": "number"
        }
    },
    "required": [
        "full_name",
        "password",
        "student_number"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "student_number": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Notes**

PUT the required parameters to permanently register a new player

* `full_name`: Full name of the student
* `password`: Password for future logins
* `student_number`: Student number of the player



<br>
<br>

# /api/player/sessions/?

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "array"
}
```



**Notes**

(Player only) GET to retrieve session objects participated
in/registered for



<br>
<br>

# /api/player/studentsessions/\(?P\<student\_number\>\[a\-zA\-Z0\-9\_\]\+\)/?$

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "array"
}
```


**Output Example**
```json
[
    1,
    56,
    7859
]
```


**Notes**

(Employees only) GET to retrieve IDs of sessions participated
in/registered for by student with `student_number`



<br>
<br>

# /api/session/session/\(?P\<session\_id\>\[a\-zA\-Z0\-9\_\]\+\)/?$

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "properties": {
        "end_time": {
            "type": "number"
        },
        "results": {
            "type": [
                "string",
                "null"
            ]
        },
        "session_id": {
            "type": "number"
        },
        "sport_id": {
            "type": "number"
        },
        "start_time": {
            "type": "number"
        },
        "venue_name": {
            "type": "string"
        }
    },
    "type": "object"
}
```



**Notes**

GET data for session with `session_id`



## PUT


**Input Schema**
```json
{
    "properties": {
        "end_time": {
            "type": "number"
        },
        "sport_id": {
            "type": "number"
        },
        "start_time": {
            "type": "number"
        },
        "venue_name": {
            "type": "string"
        }
    },
    "required": [
        "start_time",
        "end_time",
        "sport_id",
        "venue_name"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "session_id": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Notes**

PUT to create a new session

* `start_time`: Time session starts in Unix Time
* `end_time`: Time session ends in Unix Time
* `sport_id`: ID of sport this session is for
* `venue_name`: Name of venue where this session is held



## PATCH


**Input Schema**
```json
{
    "properties": {
        "results": {
            "type": "string"
        },
        "session_id": {
            "type": "number"
        }
    },
    "required": [
        "session_id",
        "results"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "session_id": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Notes**

PATCH to add/amend results for a session

* `results`: String noting results of a session



## DELETE


**Input Schema**
```json
null
```



**Output Schema**
```json
null
```



**Notes**

(Employees Only) DELETE session with `session_id`
    (cascade through teams for that session)



<br>
<br>

# /api/session/session/?

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "properties": {
        "end_time": {
            "type": "number"
        },
        "results": {
            "type": [
                "string",
                "null"
            ]
        },
        "session_id": {
            "type": "number"
        },
        "sport_id": {
            "type": "number"
        },
        "start_time": {
            "type": "number"
        },
        "venue_name": {
            "type": "string"
        }
    },
    "type": "object"
}
```



**Notes**

GET data for session with `session_id`



## PUT


**Input Schema**
```json
{
    "properties": {
        "end_time": {
            "type": "number"
        },
        "sport_id": {
            "type": "number"
        },
        "start_time": {
            "type": "number"
        },
        "venue_name": {
            "type": "string"
        }
    },
    "required": [
        "start_time",
        "end_time",
        "sport_id",
        "venue_name"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "session_id": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Notes**

PUT to create a new session

* `start_time`: Time session starts in Unix Time
* `end_time`: Time session ends in Unix Time
* `sport_id`: ID of sport this session is for
* `venue_name`: Name of venue where this session is held



## PATCH


**Input Schema**
```json
{
    "properties": {
        "results": {
            "type": "string"
        },
        "session_id": {
            "type": "number"
        }
    },
    "required": [
        "session_id",
        "results"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "session_id": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Notes**

PATCH to add/amend results for a session

* `results`: String noting results of a session



## DELETE


**Input Schema**
```json
null
```



**Output Schema**
```json
null
```



**Notes**

(Employees Only) DELETE session with `session_id`
    (cascade through teams for that session)



<br>
<br>

# /api/session/sessions/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "ended_before": {
            "type": "number"
        },
        "sports": {
            "type": "array"
        },
        "started_after": {
            "type": "number"
        },
        "venues": {
            "type": "array"
        }
    },
    "type": "object"
}
```



**Output Schema**
```json
{
    "type": "array"
}
```



**Notes**

GET array of sessions matching given parameters

* `started_after`: Filter only sessions with a start_time greater than this (Unix Time)
* `end_before`: Filter only sessions with an end_time smaller than this (Unix Time)
* `sports`: Array of sport names; filter only sessions for these sports
* `venues`: Array of venue names; filter only sessions held in these venues



<br>
<br>

# /api/sport/sports/?

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "array"
}
```


**Output Example**
```json
[
    {
        "name": "Basketball",
        "sport_id": 1
    },
    {
        "name": "Futsal",
        "sport_id": 2
    }
]
```


**Notes**

GET array of all sports



<br>
<br>

# /api/team/players/\(?P\<team\_id\>\[a\-zA\-Z0\-9\_\]\+\)/?$

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "array"
}
```



**Notes**

GET array of players that are in `team_id`



<br>
<br>

# /api/team/register/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "team_id": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "team_id": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Notes**

(Student only) POST to register self in Team with given `team_id`

* `team_id`: ID of team to register in



<br>
<br>

# /api/team/team/?

    Content-Type: application/json

## PUT


**Input Schema**
```json
{
    "properties": {
        "name": {
            "type": "string"
        },
        "num_max_players": {
            "type": "number"
        },
        "session_id": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "team_id": {
            "type": "number"
        }
    },
    "type": "object"
}
```



**Notes**

(Employees Only) Create a team for a session

* `name`: Name of team
* `num_max_players`: Maximum number of players that can join this team
* `session_id`: ID of session which this team is for



<br>
<br>

# /api/team/teams/\(?P\<session\_id\>\[a\-zA\-Z0\-9\_\]\+\)/?$

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "array"
}
```


**Output Example**
```json
[
    {
        "name": "The Team",
        "num_max_players": 8,
        "session_id": 5,
        "team_id": 1
    }
]
```


**Notes**

GET array of all teams for the given `session_id`



<br>
<br>

# /api/venue/venue/\(?P\<venue\_name\>\[a\-zA\-Z0\-9\_\]\+\)/?$

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "properties": {
        "address": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "type": "object"
}
```



**Notes**

GET data for venue with ``venue_name``



## PUT


**Input Schema**
```json
{
    "properties": {
        "address": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "required": [
        "name",
        "address"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "name": {
            "type": "string"
        }
    },
    "type": "object"
}
```



**Notes**

PUT to add new venue



<br>
<br>

# /api/venue/venue/?

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "properties": {
        "address": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "type": "object"
}
```



**Notes**

GET data for venue with ``venue_name``



## PUT


**Input Schema**
```json
{
    "properties": {
        "address": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "required": [
        "name",
        "address"
    ],
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "name": {
            "type": "string"
        }
    },
    "type": "object"
}
```



**Notes**

PUT to add new venue



<br>
<br>

# /api/venue/venues/?

    Content-Type: application/json

## GET


**Input Schema**
```json
null
```



**Output Schema**
```json
{
    "type": "array"
}
```



**Notes**

GET all venues


