import pyhubb
import fire

class pyhubbcli():
    """
    Command Line Interface (CLI) to the pyhubb python package for Hubb.me's API
    """
    def __init__(self):
        pass
       
    def create(self, eventid: str, accessToken: str, expiry:str, version: str = 'v1'):
        """
        Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
        :param eventid: four digit code given by account manager
        :param accessToken: the value from the initial handshake done with postman
        :param expiry: number (in seconds) which is when your authentication will expire
        :param version: API version, set by default to v1
        """
        tokentype = 'bearer'
        apiclient = pyhubb.client(eventid, accessToken, tokentype, expiry, version)
        print('Client created! Pickled locally')
        
    def request(self, section: str, query: str, fields: str):
        """
        Make requests to the Hubb API at various endpoints (or sections) with various OData query parameters and delimiting fields
        :param section: or endpoint. The part of the Hubb site you wish to get data from. Some examples are: Sessions, Locations, Users, Sponsors, etc. More can be found at https://ngapi.hubb.me/swagger/ui/index
        :param fields: fields vary with the endpoint selected. View the docs at https://ngapi.hubb.me/swagger/ui/index for more information, these are all GET requests.
        :param query: Options which allow you to 'expand' a data field for details, 'filter' the data to what you want to see, 'select' to limit data fields returned, 'order' data by certain parameters, or limit the data to the 'top' X results (put your number in the fields parameter)
        """
        pyhubb.exists('client.pickle')
        apiclient = pyhubb.client.load_object('client.pickle')
        # no switch statement in python, if elif go brrr
        if query == 'expand':
            apiclient.expand(section, fields)
            pass
        elif query == 'filter':
            apiclient.filt(section, fields)
            pass
        elif query == 'select':
            apiclient.select(section, fields)
            pass
        elif query == 'order':
            apiclient.orderBy(section, fields)
            pass
        elif query == 'top':
            apiclient.top(section, fields)
            pass
        else:
            print('Not a valid odata query')
            pass

if __name__ == "__main__":
    fire.core.Display = lambda lines, out: print(*lines, file=out) #hacky solution to get fire to print to stdout
    fire.Fire(pyhubbcli)
