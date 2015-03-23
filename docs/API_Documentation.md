**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

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


