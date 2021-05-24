import pyhubb
import pickle
import fire
import os.path as path
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
    file_time = path.getmtime(filename)
    if ((time.time() - file_time) / 3600 > 23):
        return true # Should use this boolean to delete the pickle file and make a new one
    else:
        return false # Should use this boolean to use the existing pickle

class pyhubbcli:
    """
    Command Line Interface (CLI) to the pyhubb python package for Hubb.me's API
    """
    def init(self, eventID: str, accessToken: str, expiry:str, version: str = 'v1'):
        """
        Initializes client object with Hubb.me API endpoint data. Use Postman to get your accessToken.
        :param eventID: aka 'scope' or a value which represents which Hubb site this client works on
        :param accessToken: the value from the initial handshake done with postman
        :param expiry: number (in seconds) which is when your authentication will expire
        :param version: API version, set by default to v1
        """
        client = pyhubb(eventID, accessToken, 'bearer', expiry, version)
        save_object(client)

if __name__ == "__main__":
    fire.Fire(pyhubbcli)
