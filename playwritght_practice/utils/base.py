
import json

class Base:

    @staticmethod
    def get_credentials():
        with open('data/credentials.json') as f:
            credentials = json.load(f)
        return credentials['user_credentials']

