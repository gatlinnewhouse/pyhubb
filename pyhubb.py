import pyodata
import requests
import json

class HubbSite :
    def __init__(self):
        print("Apply for Hubb API Access here: https://apirequest.hubb.me/")
    
    """ unsure about return variables here """
    def authHandshake(clientID: string, clientSecret: string, scope: string) -> string,string,string:
        url = 'https://ngapi.hubb.me/auth/token'
        creds = {'client_id': clientID, 'client_secret': clientSecret, 'scope': scope}
        res = requests.post(url, data = creds, headers = {"Content-Type": "application/x-www-form-urlencoded"})
        resp = json.load(res)
        """ not sure this json reading works """
        for p in resp:
            accessToken = (p['access_token'])
            tokenType = (p['token_type'])
            expiry = (p['expires_in'])
        return acessToken, tokenType, expiry
    
    """ how does odata request work with authentication? """
    def odataURL(serviceURL: string) -> pyodata.Client :
        SERVICE_URL = serviceURL
        HTTP_LIB = requests.Session()
        return pyodata.Client(SERVICE_URL, HTTP_LIB)