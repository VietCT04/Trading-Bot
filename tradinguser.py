import uuid
import json
import os
from user import User

class TradingUser(User):
    def __init__(self, username, password, apikey, secretkey):
        super.__init__(username, password)
        self.username = username
        self._password = password