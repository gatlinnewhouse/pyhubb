# pyhubb
Python API library for Hubb.me

### Example CLI

Initializing session after using postman to get API credentials, like an access token.
```bash
gat@DESKTOP-CD2M3FT:Documents$ python pyhubb_cli.py create 'put your 4 digit event id here' 'put your api access token here' 'put your expiry here'
Client created! Pickled locally                                
```
Message returns that a client object for the API credentials was made and then saved locally.

Example request and response:
```bash
gat@DESKTOP-CD2M3FT:Documents$ python pyhubb_cli.py request Sessions top 1
VERIFIED: Client data is not expired!
[
  {
    "Id": REDACTED,
    "Title": "Cookin Chicken 101",
    "Description": "An introduction to food chemistry",
    "Mandatory": null,
    "Enabled": true,
    "CanBeEvaluated": null,
    "VideoLink": null,
    "Code": "CHCKN101",
    "TrackId": REDACTED,
    "TimeSlotId": REDACTED,
    "RoomId": REDACTED,
    "DeckLink": null,
    "IsFeatured": false,
    "SessionTypeId": REDACTED,
    "VisibleToAnonymousUsers": false,
    "VisibleInSessionListing": true,
    "Status": "Accepted",
    "LastModified": {
      "UTC": "2021-04-12T18:53:12Z",
      "EventTime": "2021-04-12T11:53:12-07:00"
  },
  "Links": null,
  "SpeakerOrder": [
    "REDACTED",
    "REDACTED"
    ],
    "LastModifiedById": REDACTED,
    "AttendeeCount": 0,
    "IsSessionComplete": 0,
    "CanUserModifySchedule": false,
    "UserPermission": "Read",
    "WaitlistCapacity": null,
    "WaitlistedCount": 0,
    "IsLocked": false,
    "SessionGroupId": null,
    "OnScheduleURL": null,
    "SessionType": null,
    "TimeSlot": null,
    "Track": null,
    "Speakers": [],
    "PropertyValues": [],
    "Assistants": [],
    "Graders": [],
    "SessionOwners": [],
    "AllowedCustomRoles": [],
    "Room": null,
    "SessionRequests": [],
    "SessionGroup": null,
    "ChatRooms": []
  }
]               
```
The library function for requests will also return a json that you can parse/save/etc.

#### Help Messages
```bash
gat@DESKTOP-CD2M3FT:Documents$ python pyhubb_cli.py
NAME
  pyhubb_cli.py - Command Line Interface (CLI) to the pyhubb python package for Hubb.me's API
SYNOPSIS
  pyhubb_cli.py COMMAND
DESCRIPTION
  Command Line Interface (CLI) to the pyhubb python package for Hubb.me's API
  COMMANDS
    COMMAND is one of the following:
      create
        Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
      request
        Make requests to the Hubb API at various endpoints (or sections) with various OData query parameters and delimiting fields 
```

```bash
gat@DESKTOP-CD2M3FT:Documents$ python pyhubb_cli.py create -h
INFO: Showing help with the command 'pyhubb_cli.py create -- --help'.

NAME
  pyhubb_cli.py create - Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
  
SYNOPSIS
  pyhubb_cli.py create EVENTID ACCESSTOKEN EXPIRY <flags>
  
DESCRIPTION
  Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.

POSITIONAL ARGUMENTS
  EVENTID
    Type: str
    four digit code given by account manager
  ACCESSTOKEN
    Type: str
    the value from the initial handshake done with postman
  EXPIRY
    Type: str
    number (in seconds) which is when your authentication will expire

FLAGS
  --version=VERSION
    Type: str
    Default: 'v1'
    API version, set by default to v1

NOTES
  You can also use flags syntax for POSITIONAL ARGUMENTS    
```

```bash
gat@DESKTOP-CD2M3FT:Documents$ python pyhubb_cli.py request -h
INFO: Showing help with the command 'pyhubb_cli.py request -- --help'.

NAME
  pyhubb_cli.py request - Make requests to the Hubb API at various endpoints (or sections) with various OData query parameters and delimiting fields

SYNOPSIS
  pyhubb_cli.py request SECTION QUERY FIELDS

DESCRIPTION
  Make requests to the Hubb API at various endpoints (or sections) with various OData query parameters and delimiting fields

POSITIONAL ARGUMENTS
  SECTION
    Type: str
    or endpoint. The part of the Hubb site you wish to get data from. Some examples are: Sessions, Locations, Users, Sponsors, etc. More can be found at https://ngapi.hubb.me/swagger/ui/index
  QUERY
    Type: str
    Options which allow you to 'expand' a data field for details, 'filter' the data to what you want to see, 'select' to limit data fields returned, 'order' data by certain parameters, or limit the data to the 'top' X results (put your number in the fields parameter)
  FIELDS
    Type: str
    fields vary with the endpoint selected. View the docs at https://ngapi.hubb.me/swagger/ui/index for more information, these are all GET requests.

NOTES
  You can also use flags syntax for POSITIONAL ARGUMENTS    
```
