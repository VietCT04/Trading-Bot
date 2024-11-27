import uuid
import json
import os
from user import User  # Assuming User class is in user.py


class TradingUser(User):
    """Represents a Trading User with private attributes for sensitive data."""

    def __init__(self, username, password, apikey, secretkey):
        """
        Initializes a new trading user with sensitive data stored as private attributes.
        
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
            apikey (str): The API key for trading.
            secretkey (str): The secret key for trading.
            trading_balance (float): Initial trading balance (default is 0.0).
        """
        super().__init__(username, password)  # Initialize attributes from User
        self._apikey = apikey  # Private API key
        self._secretkey = secretkey  # Private secret key

    @classmethod
    def sign_up(cls, username, password, apikey, secretkey):
        """
        Overrides the User sign_up method to include sensitive keys for trading users.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
            apikey (str): The API key for the trading user.
            secretkey (str): The secret key for the trading user.

        Returns:
            TradingUser: The newly created TradingUser object if sign-up is successful.
            None: If the username already exists.
        """
        if username in cls.credentials:
            print("Username already exists for TradingUser.")
            return None  # Username already exists

        # Create a new TradingUser
        new_trading_user = cls(username, password, apikey, secretkey)  # Default balance
        cls.credentials[username] = {
            "password": password,
            "apikey": apikey,
            "secretkey": secretkey,
        }  # Store credentials with sensitive keys
        cls._save_to_file()  # Save to JSON file

        print(f"TradingUser '{username}' created.")
        return new_trading_user
