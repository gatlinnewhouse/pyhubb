# pyhubb
Python API library for Hubb.me

### Example CLI
```bash
NAME                     
  pyhubb_cli.py - Command Line Interface (CLI) to the pyhubb python package for Hubb.me's API
SYNOPSIS 
  pyhubb_cli.py COMMAND                                                                                                                                                           
DESCRIPTION                     
  Command Line Interface (CLI) to the pyhubb python package for Hubb.me's API
  COMMANDS
    COMMAND is one of the following:
      init
        Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
```

```bash
NAME
  pyhubb_cli.py init - Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
SYNOPSIS
  pyhubb_cli.py init EVENTID ACCESSTOKEN EXPIRY <flags>
DESCRIPTION
  Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
POSITIONAL ARGUMENTS
  EVENTID
    Type: str
      aka 'scope' or a value which represents which Hubb site this client works on
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
