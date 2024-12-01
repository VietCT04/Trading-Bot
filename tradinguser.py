import uuid
import json
import os
from user import User


class TradingUser(User):

    def __init__(self, username, password, apikey, secretkey):
        super().__init__(username, password) 
        self._apikey = apikey 
        self._secretkey = secretkey 

    @classmethod
    def sign_up(cls, username, password, apikey, secretkey):
        if username in cls.credentials:
            print("Username already exists for TradingUser.")
            return None 

        new_trading_user = cls(username, password, apikey, secretkey)  
        cls.credentials[username] = {
            "password": password,
            "apikey": apikey,
            "secretkey": secretkey,
        } 
        cls._save_to_file() 

        print(f"TradingUser '{username}' created.")
        return new_trading_user
