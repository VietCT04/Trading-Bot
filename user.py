import uuid
class User:
    def __init__(self, username):
        self.username = username
        self._user_id = str(uuid.uuid4())
        