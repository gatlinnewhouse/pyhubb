import requests
import json

class HubbSite :
    def __init__(self):
        print("Apply for Hubb API Access here: https://apirequest.hubb.me/")
    
    """ unsure about return variables here """
    def authHandshake(clientID: string, clientSecret: string, scope: string) -> string,string,string:
        url = 'https://ngapi.hubb.me/auth/token'
        creds = {'client_id': clientID, 'client_secret': clientSecret, 'scope': scope, 'grant_type': 'client_credentials'}
        res = requests.post(url, data = creds, headers = {"Content-Type": "application/x-www-form-urlencoded"})
        resp = json.load(res)
        print(resp.json())
        """ not sure this json reading works """
        for p in resp:
            accessToken = (p['access_token'])
            tokenType = (p['token_type'])
            expiry = (p['expires_in'])
        return accessToken, tokenType, expiry

class client :
    def __init__(eventID, accessToken, tokenType, expiry, version):
        self.url = 'https://ngapi.hubb.me/api/' + version + '/' + eventID + '/'
        HTTP_LIB = requests.Session()
        self.accessToken = accessToken
        self.tokenType = tokenType
        self.expiry = expiry
        self.headers = {'Authorization': 'Bearer' + accessToken, 'Content-Type': 'application/json'}
    """ This allows you to expand a data field. """
    """ If you're seeing a value of NULL or an empty array, 
    but you expect there should be data, try "expanding" that value. """
    def expand(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$expand=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    """ This allows you to filter the data to only what you want to see. """
    """ Only items where the expression evaluates to TRUE are included in the response. """
    def filt(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$filter=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    """ This can be used to limit the data fields with are returned with a call. 
    You can select only certain fields to come through. """
    def select(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$select=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    """ This will allow you to order the data by a certain parameter. """
    def orderBy(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$orderby=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    """ This will allow you to limit the data that gets returned to a specific number. """
    def top(self, section, fields) -> json:
        details = requests.get(self.url + section + '?$top=' + fields, headers=self.headers)
        print(details.json())
        return details.json()
    """ myConference grabs all the events/sessions on a given users schedule """
    """ It's recommended that you get the items for an individual user at a time. """
    """ This will prevent the system from lagging as it tries to return an abundance of data. """
    """ Note: The API is limited to only return 1000 items at a time. You can use the $top and
    $skip parameters to create a loop that will get all items. """
    def myConference(self, attendeeID) -> json:
        details = requests.get(self.url + 'Myconference?$filter=AttendeeId eq ' + attendeeID, headers=self.headers)
        print(details.json())
        return details.json()