from typing import Dict, Any


class User:
    """User class keeps user object from database"""
    def __init__(self, args) -> None:
        self._id = args[0]
        self.username = args[1]
        self.token = args[2]
        self.room = args[3]
    
    def __str__(self) -> str:
        return f'{self._id} {self.username} in {self.room} room. {self.token}'
    
    def json(self) -> Dict[str, Any]:
        """Returns json representation of User"""
        return {
            'id': self._id,
            'username': self.username,
            'token': self.token,
            'room': self.room
        }
