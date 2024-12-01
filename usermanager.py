import uuid
import json
import os
from user import User

class UserManager:

    credentials_file = "credentials.json"

    credentials = {}

    if os.path.exists(credentials_file):
        with open(credentials_file, "r") as f:
            credentials = json.load(f)
    else:
        credentials = {}

    def __init__(self, username, password):
        self.username = username
        self._password = password
        self._user_id = str(uuid.uuid4()) 

    @property
    def user_id(self):
        return self._user_id

    @classmethod
    def authenticate(cls, username, password):
        if os.path.exists(cls.credentials_file):
            with open(cls.credentials_file, "r") as f:
                cls.credentials = json.load(f)
        else:
            cls.credentials = {}
        return cls.credentials.get(username)["password"] == password

    @classmethod
    def sign_up(cls, username, password):
        if username in cls.credentials:
            return None 

        new_user = User(username, password)
        cls.credentials[username]["password"] = password

        cls._save_to_file()

        return new_user

    @classmethod
    def _save_to_file(cls):
        with open(cls.credentials_file, "w") as f:
            json.dump(cls.credentials, f, indent=4)

