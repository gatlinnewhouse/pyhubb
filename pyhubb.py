import requests
import json
import pickle
import os
import time

# Pickling to cache data while CLI runs.
def save_object(obj):
    try:
        with open("client.pickle", "wb") as f:
            pickle.dump(obj, f)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

# Open the pickle jar to grab the client info
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            myinstance = pickle.load(f)
        for k in myinstance.__dict__.keys():
            setattr(client, k, getattr(myinstance, k))
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

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

class client(object):
    # Create client
    def __init__(self, eventID, accessToken, tokenType, expiry, version):
        self.url = 'https://ngapi.hubb.me/api/' + str(version) + '/' + str(eventID) + '/'
        HTTP_LIB = requests.Session()
        self.accessToken = accessToken
        self.tokenType = tokenType
        self.expiry = expiry
        self.headers = {'Authorization': 'Bearer' + accessToken, 'Content-Type': 'application/json'}
        save_object(self)
    # This allows you to expand a data field.
    # If you're seeing a value of NULL or an empty array, 
    # but you expect there should be data, try "expanding" that value.
    def expand(self, section, fields) -> json:
        exists('client.pickle')
        load_object('client.pickle')
        details = requests.get(self.url + section + '?$expand=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    # This allows you to filter the data to only what you want to see.
    # Only items where the expression evaluates to TRUE are included in the response.
    def filt(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$filter=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    # This can be used to limit the data fields with are returned with a call. 
    # You can select only certain fields to come through.
    def select(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$select=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    # This will allow you to order the data by a certain parameter.
    def orderBy(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$orderby=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    # This will allow you to limit the data that gets returned to a specific number.
    def top(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$top=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    # myConference grabs all the events/sessions on a given users schedule
    # It's recommended that you get the items for an individual user at a time.
    # This will prevent the system from lagging as it tries to return an abundance of data.
    # Note: The API is limited to only return 1000 items at a time. You can use the $top and
    # $skip parameters to create a loop that will get all items.
    def myConference(self, attendeeID) -> json:
        details = requests.get(self.url + 'Myconference?$filter=AttendeeId eq ' + attendeeID, headers=self.headers)
        print(details.json())
        return details.json()

