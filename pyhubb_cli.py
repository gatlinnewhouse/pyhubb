import pyhubb
import pickle
import fire
import os
import time

# Pickling to cache data while CLI runs
def save_object(obj):
    try:
        with open("client.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

# Open the pickle jar to grab the client info
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
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

def exists(filename):
    if os.path.exists(filename):
        age = expired_object(filename)
        if age == True:
            os.remove(filename)
            print("WARNING: Client data expired! Removed old pickled credentials. Run pyhubb_cli init\n")
        else:
            print("VERIFIED: Client data is not expired!\n")
    else:
        raise Exception("Client data pickle does not exist! Run pyhubb_cli init\n")

class pyhubbcli:
    """
    Command Line Interface (CLI) to the pyhubb python package for Hubb.me's API
    """
    def __init__(self):
        pass
       
    def init(eventID: str, accessToken: str, expiry:str, version: str = 'v1'):
        """
        Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
        :param eventID: aka 'scope' or a value which represents which Hubb site this client works on
        :param accessToken: the value from the initial handshake done with postman
        :param expiry: number (in seconds) which is when your authentication will expire
        :param version: API version, set by default to v1
        """
        apiclient = pyhubb.client(eventID, accessToken, 'bearer', expiry, version)
        save_object(apiclient)
    def request(fields: str, section: str = 'Sessions', query: str = 'expand'):
        """
        Make requests to the Hubb API at various endpoints (or sections) with various OData query parameters and delimiting fields
        :param fields: fields vary with the endpoint selected. View the docs at https://ngapi.hubb.me/swagger/ui/index for more information, these are all GET requests.
        :param section: or endpoint. The part of the Hubb site you wish to get data from. Some examples are: Sessions, Locations, Users, Sponsors, etc. More can be found at https://ngapi.hubb.me/swagger/ui/index
        :param query: Options which allow you to 'expand' a data field for details, 'filter' the data to what you want to see, 'select' to limit data fields returned, 'order' data by certain parameters, or limit the data to the 'top' X results (put your number in the fields parameter)
        """
        exists('client.pickle')
        apiclient = load_object('client.pickle')

if __name__ == "__main__":
    fire.core.Display = lambda lines, out: print(*lines, file=out) #hacky solution to get fire to print to stdout
    fire.Fire(pyhubbcli)
