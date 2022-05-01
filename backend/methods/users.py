from fastapi import FastAPI, WebSocketDisconnect, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from utils import gen_token
from errors import Errors
from .database import Message, db
from .websocket_manager import WebsocketManager


manager = WebsocketManager()
users = FastAPI()
users.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUCCESS = {'response': 'success'}


@users.get('/new')
async def create_user(name: str):
    """Creates a new user."""
    if await db.has_user(name):
        return Errors.USERNAME_IS_EXISTS
    token = await gen_token()
    await db.add_user(name, token)
    return {'response': {'username': name, 'token': token}}


@users.get('/get')
async def get_user(token: str):
    """This function returns user data"""
    if not await db.has_user_by_token(token):
        return Errors.USER_IS_NOT_EXISTS
    user = await db.get_user(token)
    return {'response': user.json()}


@users.get('/remove')
async def remove_user(token: str):
    """Removes user from database"""
    if not await db.has_user_by_token(token):
        return Errors.USER_IS_NOT_EXISTS
    user = await db.get_user(token)
    if user.room:
        message = Message(
            f'{user.username} left from chat',
            user.username,
            Message.Action.LEFT_FROM_CHAT
        )
        await manager.broadcast_to_room(message, db, user.room)
        room = await db.get_room(user.room)
        room.users.remove(user._id)
        await db.save_room(room)
    await db.remove_user(token)


@users.get('/getall')
async def get_all_users():
    """This returns all users"""
    users = await db.get_users()
    return {
        'response': [{
            'id': i._id,
            'username': i.username,
            'token': i.token
        } for i in users]
    }


@users.get('/messages.send')
async def user_send_message(text: str, token: str):
    """Sends message to the room"""
    if not await db.has_user_by_token(token):
        return Errors.USER_IS_NOT_EXISTS
    if not text:
        return Errors.TEXT_IS_EMPTY
    user = await db.get_user(token)
    if not user.room:
        return Errors.USER_HASNOT_ROOM
    room = await db.get_room(user.room)
    message = Message(
        text,
        user.username
    )
    await db.save_room(room)
    await manager.broadcast_to_room(message, db, room.token)
    return SUCCESS


@users.websocket("/poll")
async def websocket_endpoint(websocket: WebSocket, token: str):
    """Long polling events"""
    if not await db.has_user_by_token(token):
        return
    user = await db.get_user(token)
    if not user.room:
        return
    await manager.connect(websocket, user.token, user.room)
    try:
        while True:
            text = await websocket.receive_text()
            message = Message(
                text,
                user.username
            )
            room = await db.get_room(user.room)
            await manager.send_personal(websocket, SUCCESS)
            await manager.broadcast_to_room(message, db, room.token)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        message = Message(
            f'{user.username} left from chat',
            user.username,
            Message.Action.LEFT_FROM_CHAT
        )
        await manager.broadcast_to_room(message, db, user.token)


@users.get('/room.enter')
async def enter_in_room(token: str, room_token: str):
    """Changes current user's room"""
    if not await db.has_user_by_token(token):
        return Errors.USER_IS_NOT_EXISTS
    if not await db.has_room_by_token(room_token):
        return Errors.ROOM_IS_NOT_EXISTS
    user = await db.get_user(token)
    if user.room:
        room = await db.get_room(user.room)
        message = Message(
            f'{user.username} left from chat',
            user.username,
            Message.Action.LEFT_FROM_CHAT
        )
        await manager.broadcast_to_room(message, db, user.room)
        room.users.remove(user._id)
        await db.save_room(room)
    room = await db.get_room(room_token)
    if room.users_limit == len(room.users):
        return Errors.ROOM_IS_FULL
    room.add_user(user._id)
    user.room = room_token
    message = Message(
        f'{user.username} join the chat',
        user.username,
        Message.Action.JOIN_THE_CHAT
    )
    await db.save_room(room)
    await db.save_user(user)
    await manager.broadcast_to_room(message, db, room_token)
    return SUCCESS


@users.get('/room.leave')
async def leave_from_room(token: str):
    """Deletes current user's room."""
    if not await db.has_user_by_token(token):
        return Errors.USER_IS_NOT_EXISTS
    user = await db.get_user(token)
    if user.room:
        message = Message(
            f'{user.username} left from chat',
            user.username,
            Message.Action.LEFT_FROM_CHAT
        )
        await manager.broadcast_to_room(message, db, user.room)
        room = await db.get_room(user.room)
        room.users.remove(user._id)
        await db.save_room(room)
        return SUCCESS
    return Errors.USER_HASNOT_ROOM
