from json import loads, dumps
from typing import NoReturn, List, Dict, Any

from .message import Message


class Room:
    """Room class keeps room object from database"""
    def __init__(self, args) -> None:
        self._id = args[0]
        self.name = args[1]
        self.token = args[2]
        self.history: List[Dict[Any]] = loads(args[3])
        self.users: List[int] = loads(args[4])
        self.users_limit: int = args[5]
    
    def add_user(
            self,
            _id: int
    ) -> NoReturn:
        self.users.append(_id)
    
    def add_msg(
            self,
            msg: Message
    ) -> NoReturn:
        self.history.append(msg.json())
    
    def __str__(self) -> str:
        return f'{self._id} {self.name}. {self.token}'
    
    def json(self) -> Dict[str, Any]:
        """Returns json representation of Room"""
        return {
            'id': self._id,
            'name': self.name,
            'token': self.token,
            'users': self.users,
            'users_limit': self.users_limit,
            'history': self.history
        }
