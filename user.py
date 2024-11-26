import uuid
import json
import os

class User:
    """Represents a User with a unique user ID and credentials stored in a JSON file."""

    # Path to the JSON file storing user credentials
    credentials_file = "credentials.json"

    # Class-level credentials dictionary
    credentials = {}

    # Load credentials from the JSON file at the start
    if os.path.exists(credentials_file):
        with open(credentials_file, "r") as f:
            credentials = json.load(f)
    else:
        credentials = {}

    def __init__(self, username, password):
        """
        Initializes a new user with a username, password, and unique user ID.
        
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.username = username
        self.password = password
        self._user_id = str(uuid.uuid4())  # Generate a unique ID for the user

    @property
    def user_id(self):
        """Returns the user's unique ID."""
        return self._user_id

    @classmethod
    def authenticate(cls, username, password):
        """
        Authenticates the user by checking the credentials.
        
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        
        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        return cls.credentials.get(username) == password

    @classmethod
    def sign_up(cls, username, password):
        """
        Allows a new user to sign up by adding credentials and updating the JSON file.
        
        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
        
        Returns:
            User: The newly created User object if sign-up is successful.
            None: If the username already exists.
        """
        if username in cls.credentials:
            return None  # Username already exists

        # Create a new user and store their credentials
        new_user = User(username, password)
        cls.credentials[username] = password

        # Update the credentials JSON file
        cls._save_to_file()

        return new_user

    @classmethod
    def _save_to_file(cls):
        """Saves the current credentials dictionary to the JSON file."""
        with open(cls.credentials_file, "w") as f:
            json.dump(cls.credentials, f, indent=4)

