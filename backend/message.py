from typing import Dict, Any


class Message(dict):
    def __init__(
            self,
            text: str,
            author: str,
            action: str = 'send message',
            action_code: int = 1
    ) -> None:
        self.text = text
        self.author = author
        self.action = action
        self.action_code = action_code
    
    def json(self) -> Dict[str, Any]:
        return {
            'text': self.text,
            'author': self.author,
            'action': self.action,
            'action_code': self.action_code
        }
