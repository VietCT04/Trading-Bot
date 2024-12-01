import uuid
import json
import os

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password