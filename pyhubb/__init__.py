import requests
import json
import collections
import pickle
import os
import time

# Pickling to cache data while CLI runs.
def save_object(obj):
    try:
        with open(".client.pickle", "wb") as f:
            pickle.dump(obj, f)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

# Are the pickled client info objs expired?
def expired_object(filename):
    file_time = os.path.getmtime(filename)
    if ((time.time() - file_time) / 3600 > 23):
        # Should use this boolean to delete the pickle file and make a new one
        return True
    else:
        # Should use this boolean to use the existing pickle
        return False

# Does this pickled obj exist?
def exists(filename):
    if os.path.exists(filename):
        age = expired_object(filename)
        if age == True:
            os.remove(filename)
            print("WARNING: Client data expired! Removed old pickled credentials. Run pyhubb_cli create\n")
        else:
            print("VERIFIED: Client data is not expired!\n")
    else:
        raise Exception("Client data pickle does not exist! Run pyhubb_cli create\n")

# Prettyprint JSON to terminal
def prettyJson(respon):
    print(json.dumps(respon.json(), indent=4))

# Authentication workflow for getting a bearer token
# - Returns an authentication token, token type, and expiry as python dict
def auth(clientId, clientSecret, scopeNum):
    grantType = "client_credentials"
    endpoint = "https://ngapi.hubb.me/auth/token"
    requestBody = {
        "client_id": f"{clientId}",
        "client_secret": f"{clientSecret}",
        "scope": f"{scopeNum}",
        "grant_type": f"{grantType}"
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(endpoint, data=requestBody, headers=headers)
    authdict = json.loads(json.dumps(response.json(), indent=4))
    return authdict

class client(object):
    # Create client
    def __init__(self, eventID, accessToken, tokenType, expiry, version):
        self.eventID = eventID
        self.accessToken = accessToken
        self.tokenType = tokenType
        self.expiry = expiry
        self.version = version
        self.headers = {'Authorization': 'bearer ' + accessToken, 'Content-Type': 'application/json'}
        self.url = 'https://ngapi.hubb.me/api/' + str(self.version) + '/' + str(self.eventID) + '/'
        HTTP_LIB = requests.Session()
        save_object(self)
    # Define a way to print a client obj to stdout
    def __str__(self):
        return "event ID: %s\n access token: %s\n type: %s\n expiry: %s\n version: %s\n headers: %s\n" % (self.eventID, self.accessToken, self.tokenType, self.expiry, self.version, self.headers)
    # Open the pickle jar to grab the client info
    def load_object(filename):
        try:
            with open(filename, "rb") as f:
                myinstance = pickle.loads(f.read())
                return client(myinstance.eventID, myinstance.accessToken, myinstance.tokenType, myinstance.expiry, myinstance.version)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)
    # This allows you to expand a data field.
    # If you're seeing a value of NULL or an empty array, 
    # but you expect there should be data, try "expanding" that value.
    def expand(self, section, fields) -> json:
        #print(self.url + section + '?expand=' + fields)
        details = requests.get(self.url + section + '?$expand=' + fields, headers=self.headers)
        prettyJson(details)
        return details.json()
    # This allows you to filter the data to only what you want to see.
    # Only items where the expression evaluates to TRUE are included in the response.
    def filt(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$filter=' + fields, headers=self.headers)
        prettyJson(details)
        return details.json()
    # This can be used to limit the data fields with are returned with a call. 
    # You can select only certain fields to come through.
    def select(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$select=' + fields, headers=self.headers)
        prettyJson(details)
        return details.json()
    # This will allow you to order the data by a certain parameter.
    def orderBy(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$orderby=' + fields, headers=self.headers)
        prettyJson(details)
        return details.json()
    # This will allow you to limit the data that gets returned to a specific number.
    def top(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$top=' + str(fields), headers=self.headers)
        prettyJson(details)
        return details.json()
    # myConference grabs all the events/sessions on a given users schedule
    # It's recommended that you get the items for an individual user at a time.
    # This will prevent the system from lagging as it tries to return an abundance of data.
    # Note: The API is limited to only return 1000 items at a time. You can use the $top and
    # $skip parameters to create a loop that will get all items.
    def myConference(self, attendeeID) -> json:
        details = requests.get(self.url + 'Myconference?$filter=AttendeeId eq ' + attendeeID, headers=self.headers)
        prettyJson(details)
        return details.json()
    # This will generically send a POST request
    def post(self, section, body) -> json:
        details = requests.post(self.url + section, headers=self.headers, json=body)
        prettyJson(details)
        return details.json()
    # This will generically send a PUT request
    def put(self, section, body) -> json:
        details = requests.put(self.url + section, headers=self.headers, json=body)
        prettyJson(details)
        return details.json()
    # This will generically send a DELETE request
    # Make sure to include the specific ID for what object to delete
    def delete(self, section, numId) -> json:
        details = requests.put(self.url + section + '/' + numId, headers=self.headers)
        prettyJson(details)
        return details.json()
    # This will generically send a PATCH request
    def patch(self, section, body) -> json:
        details = requests.patch(self.url + section, headers=self.headers, data=body)
        prettyJson(details)
        return details.json()
