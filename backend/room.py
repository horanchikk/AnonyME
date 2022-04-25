from json import loads, dumps
from typing import NoReturn, List, Dict, Any


class Room:
    """Room class keeps room object from database"""
    def __init__(self, args) -> None:
        self._id = args[0]
        self.name = args[1]
        self.token = args[2]
        self.history: List[Dict[Any]] = loads(args[3])
        self.users: List[int] = loads(args[4])
    
    def add_user(
            self,
            _id: int
    ) -> NoReturn:
        self.users.append(_id)
    
    def add_msg(
            self,
            msg: Dict[str, Any]
    ) -> NoReturn:
        self.history.append(msg)
    
    def __str__(self) -> str:
        return f'{self._id} {self.name}. {self.token}'
    
    def json(self) -> Dict[str, Any]:
        """Returns json representation of Room"""
        return {
            'id': self._id,
            'name': self.name,
            'token': self.token,
            'users': self.users,
            'history': self.history
        }
