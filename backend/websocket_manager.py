from typing import NoReturn, List, Dict, Any

from fastapi import WebSocket
from database import Database


class WebsocketManager:
    def __init__(self) -> NoReturn:
        self.active: List[Tuple[WebSocket, str, str]] = []
    
    async def connect(
            self,
            ws: WebSocket,
            user_token: str,
            room_token: str
    ) -> NoReturn:
        await ws.accept()
        self.active.append((ws, user_token, room_token))
    
    def disconnect(
            self,
            ws: WebSocket
    ) -> NoReturn:
        for active in self.active:
            if ws == active[0]:
                self.active.remove(active)
    
    async def send_personal(
            self,
            ws: WebSocket,
            message: Dict[str, Any]
    ) -> NoReturn:
        try:
            await ws.send_json(message)
        except RuntimeError as e:
            print(e)
    
    async def broadcast_to_room(
            self,
            message: Dict[str, Any],
            db: Database,
            token: str
    ) -> NoReturn:
        for ws, user_token, room_token in self.active:
            if room_token != token:
                continue
            room = await db.get_room(room_token)
            room.history.append(message)
            try:
                await ws.send_json(message)
                await db.save_room(room)
            except RuntimeError as e:
                print(e)
