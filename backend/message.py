from typing import Dict, Any
from time import time
from enum import Enum


class Message(dict):

    class Action(Enum):
        MESSAGE = ['send message', 1]
        JOIN_THE_CHAT = ['join the chat', 2]
        LEFT_FROM_CHAT = ['left from chat', 3]

    def __init__(
            self,
            text: str,
            author: str,
            action: Action = Action.MESSAGE
    ) -> None:
        self.text = text
        self.author = author
        self.action = action.value[0]
        self.action_code = action.value[1]
        self.time = round(time())
    
    def json(self) -> Dict[str, Any]:
        return {
            'text': self.text,
            'author': self.author,
            'action': self.action,
            'action_code': self.action_code,
            'time': self.time
        }
