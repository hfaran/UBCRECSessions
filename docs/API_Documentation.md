**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/auth/employeelogin/?

    Content-Type: application/json

## POST
**Input Schema**
```json
{
    "required": [
        "username", 
        "password"
    ], 
    "type": "object", 
    "properties": {
        "username": {
            "type": "string"
        }, 
        "password": {
            "type": "string"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "username": {
            "type": "string"
        }
    }
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
    "required": [
        "student_number", 
        "password"
    ], 
    "type": "object", 
    "properties": {
        "student_number": {
            "type": "string"
        }, 
        "password": {
            "type": "string"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "student_number": {
            "type": "string"
        }
    }
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
    "type": "object", 
    "properties": {
        "start": {
            "type": "number"
        }, 
        "end": {
            "type": "number"
        }
    }
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
    "type": "object", 
    "properties": {
        "username": {
            "type": "string"
        }, 
        "student_number": {
            "type": "number"
        }
    }
}
```

**Output Example**
```json
{
    "student_number": 10235609, 
    "full_name": "John Smith"
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
    "required": [
        "full_name", 
        "password", 
        "student_number"
    ], 
    "type": "object", 
    "properties": {
        "student_number": {
            "type": "number"
        }, 
        "password": {
            "type": "string"
        }, 
        "full_name": {
            "type": "string"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "student_number": {
            "type": "number"
        }
    }
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

**Output Example**
```json
[
    1, 
    56, 
    7859
]
```


**Notes**

(Player only) GET to retrieve IDs of sessions participated
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
    "type": "object", 
    "properties": {
        "venue_name": {
            "type": "string"
        }, 
        "start_time": {
            "type": "number"
        }, 
        "results": {
            "type": "string"
        }, 
        "session_id": {
            "type": "number"
        }, 
        "end_time": {
            "type": "number"
        }, 
        "sport_id": {
            "type": "number"
        }
    }
}
```


**Notes**

GET data for session with `session_id`



## PATCH
**Input Schema**
```json
{
    "required": [
        "session_id", 
        "results"
    ], 
    "type": "object", 
    "properties": {
        "results": {
            "type": "string"
        }, 
        "session_id": {
            "type": "number"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "session_id": {
            "type": "number"
        }
    }
}
```


**Notes**

PATCH to add/amend results for a session

* `results`: String noting results of a session



## PUT
**Input Schema**
```json
{
    "required": [
        "start_time", 
        "end_time", 
        "sport_id", 
        "venue_name"
    ], 
    "type": "object", 
    "properties": {
        "start_time": {
            "type": "number"
        }, 
        "end_time": {
            "type": "number"
        }, 
        "sport_id": {
            "type": "number"
        }, 
        "venue_name": {
            "type": "string"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "session_id": {
            "type": "number"
        }
    }
}
```


**Notes**

PUT to create a new session

* `start_time`: Time session starts in Unix Time
* `end_time`: Time session ends in Unix Time
* `sport_id`: ID of sport this session is for
* `venue_name`: Name of venue where this session is held



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
    "type": "object", 
    "properties": {
        "venue_name": {
            "type": "string"
        }, 
        "start_time": {
            "type": "number"
        }, 
        "results": {
            "type": "string"
        }, 
        "session_id": {
            "type": "number"
        }, 
        "end_time": {
            "type": "number"
        }, 
        "sport_id": {
            "type": "number"
        }
    }
}
```


**Notes**

GET data for session with `session_id`



## PATCH
**Input Schema**
```json
{
    "required": [
        "session_id", 
        "results"
    ], 
    "type": "object", 
    "properties": {
        "results": {
            "type": "string"
        }, 
        "session_id": {
            "type": "number"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "session_id": {
            "type": "number"
        }
    }
}
```


**Notes**

PATCH to add/amend results for a session

* `results`: String noting results of a session



## PUT
**Input Schema**
```json
{
    "required": [
        "start_time", 
        "end_time", 
        "sport_id", 
        "venue_name"
    ], 
    "type": "object", 
    "properties": {
        "start_time": {
            "type": "number"
        }, 
        "end_time": {
            "type": "number"
        }, 
        "sport_id": {
            "type": "number"
        }, 
        "venue_name": {
            "type": "string"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "session_id": {
            "type": "number"
        }
    }
}
```


**Notes**

PUT to create a new session

* `start_time`: Time session starts in Unix Time
* `end_time`: Time session ends in Unix Time
* `sport_id`: ID of sport this session is for
* `venue_name`: Name of venue where this session is held



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
    "type": "object", 
    "properties": {
        "started_after": {
            "type": "number"
        }, 
        "ended_before": {
            "type": "number"
        }, 
        "venues": {
            "type": "array"
        }, 
        "sports": {
            "type": "array"
        }
    }
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

# /api/team/register/?

    Content-Type: application/json

## POST
**Input Schema**
```json
{
    "type": "object", 
    "properties": {
        "team_id": {
            "type": "number"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "team_id": {
            "type": "number"
        }
    }
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
    "type": "object", 
    "properties": {
        "name": {
            "type": "string"
        }, 
        "session_id": {
            "type": "number"
        }, 
        "num_max_players": {
            "type": "number"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "team_id": {
            "type": "number"
        }
    }
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
        "team_id": 1, 
        "name": "The Team", 
        "session_id": 5, 
        "num_max_players": 8
    }
]
```


**Notes**

GET array of all teams for the given `session_id`



<br>
<br>

# /api/venue/venue/\(?P\<venue\_name\>\[a\-zA\-Z0\-9\_\]\+\)/?$

    Content-Type: application/json

## PUT
**Input Schema**
```json
{
    "required": [
        "name", 
        "address"
    ], 
    "type": "object", 
    "properties": {
        "name": {
            "type": "string"
        }, 
        "address": {
            "type": "string"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "name": {
            "type": "string"
        }
    }
}
```


**Notes**

PUT to add new venue



## GET
**Input Schema**
```json
null
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "name": {
            "type": "string"
        }, 
        "address": {
            "type": "string"
        }
    }
}
```


**Notes**

GET data for venue with ``venue_name``



<br>
<br>

# /api/venue/venue/?

    Content-Type: application/json

## PUT
**Input Schema**
```json
{
    "required": [
        "name", 
        "address"
    ], 
    "type": "object", 
    "properties": {
        "name": {
            "type": "string"
        }, 
        "address": {
            "type": "string"
        }
    }
}
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "name": {
            "type": "string"
        }
    }
}
```


**Notes**

PUT to add new venue



## GET
**Input Schema**
```json
null
```

**Output Schema**
```json
{
    "type": "object", 
    "properties": {
        "name": {
            "type": "string"
        }, 
        "address": {
            "type": "string"
        }
    }
}
```


**Notes**

GET data for venue with ``venue_name``



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


