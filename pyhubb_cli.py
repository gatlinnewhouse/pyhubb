import pyhubb
import fire

class pyhubbcli:
    """
    Command Line Interface (CLI) to the pyhubb python package for Hubb.me's API
    """
    def __init__(self):
        pass
       
    def create(eventID: str, accessToken: str, expiry:str, version: str = 'v1'):
        """
        Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
        :param eventID: aka 'scope' or a value which represents which Hubb site this client works on
        :param accessToken: the value from the initial handshake done with postman
        :param expiry: number (in seconds) which is when your authentication will expire
        :param version: API version, set by default to v1
        """
        apiclient = pyhubb.client(eventID, accessToken, 'bearer', expiry, version)
        
    def request(fields: str, section: str = 'Sessions', query: str = 'expand'):
        """
        Make requests to the Hubb API at various endpoints (or sections) with various OData query parameters and delimiting fields
        :param fields: fields vary with the endpoint selected. View the docs at https://ngapi.hubb.me/swagger/ui/index for more information, these are all GET requests.
        :param section: or endpoint. The part of the Hubb site you wish to get data from. Some examples are: Sessions, Locations, Users, Sponsors, etc. More can be found at https://ngapi.hubb.me/swagger/ui/index
        :param query: Options which allow you to 'expand' a data field for details, 'filter' the data to what you want to see, 'select' to limit data fields returned, 'order' data by certain parameters, or limit the data to the 'top' X results (put your number in the fields parameter)
        """
        pyhubb.client.expand(fields, section)

if __name__ == "__main__":
    fire.core.Display = lambda lines, out: print(*lines, file=out) #hacky solution to get fire to print to stdout
    fire.Fire(pyhubbcli)
