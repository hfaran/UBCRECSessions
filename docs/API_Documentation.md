**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

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
    "student_number": 10235609,
    "username": "john_smith"
}
```


**Notes**

GET to retrieve player info



<br>
<br>

# /api/player/player/?

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
        },
        "username": {
            "type": "string"
        }
    },
    "required": [
        "username",
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
        "username": {
            "type": "string"
        }
    },
    "type": "object"
}
```



**Notes**

POST the required parameters to permanently register a new player

* `username`: Username of the player
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

GET to retrieve IDs of sessions participated in/registered for



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
            "type": "string"
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



<br>
<br>

# /api/session/sessions/?

    Content-Type: application/json

## GET


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


