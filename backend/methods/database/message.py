from typing import Dict, Any
from time import time
from enum import Enum


class Message(dict):

    class Action(Enum):
        MESSAGE = ['send message', 1]
        JOIN_THE_CHAT = ['join the chat', 2]
        LEFT_FROM_CHAT = ['left from chat', 3]
        CREATE_ROOM = ['create room', 4]

    def __init__(
            self,
            text: str,
            author: str,
            action: Action = Action.MESSAGE,
            sticker_id: int = 0,
            reply: Dict[str, str] = {}
    ) -> None:
        self['text'] = text
        self['author'] = author
        self['action'] = action.value[0]
        self['action_code'] = action.value[1]
        self['sticker_id'] = sticker_id
        self['time'] = round(time())
        self['reply'] = reply
