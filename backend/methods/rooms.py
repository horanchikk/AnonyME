from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils import gen_token
from errors import Errors
from .database import Message, db
from .websocket_manager import manager


rooms = FastAPI()
rooms.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUCCESS = {'response': 'success'}


@rooms.get('/new')
async def create_room(
        name: str,
        user_token: str,
        users_limit: int = 2
):
    """This function creates a new room."""
    if not await db.has_user_by_token(user_token):
        return Errors.USER_IS_NOT_EXISTS.value
    token = await gen_token()
    await db.add_room(name, token, users_limit)

    user = await db.get_user(user_token)
    room = await db.get_room(token)
    room.add_user(user._id)
    message = Message(
        f'{user.username} create room',
        user.username,
        Message.Action.CREATE_ROOM
    )
    room.add_msg(message)
    user.room = token
    await db.save_room(room)
    await db.save_user(user)
    return {'response': {'name': name, 'token': token}}


@rooms.get('/get')
async def get_room(token: str):
    """This function returns room data"""
    if not await db.has_room_by_token(token):
        return Errors.ROOM_IS_NOT_EXISTS.value
    room = await db.get_room(token)
    return {'response': room.json()}


@rooms.get('/remove')
async def remove_room(token: str):
    """Removes room from database"""
    if not await db.has_room_by_token(token):
        return Errors.ROOM_IS_NOT_EXISTS.value
    room = await db.get_room(token)
    for user_id in room.users:
        user = await db.get_user(user_id)
        user.room = ''
        await db.save_user(user)
    await db.remove_room(token)


@rooms.get('/getall')
async def get_all_rooms():
    """This returns all rooms"""
    rooms = await db.get_rooms()
    return {
        'response': [{
            'id': i._id,
            'name': i.name,
            'token': i.token,
            'is_full': i.users_limit <= len(i.users),
            'users_limit': i.users_limit
        } for i in rooms]
    }


@rooms.get('/history.get')
async def get_room_history(token: str):
    """Returns room messages history"""
    if not await db.has_room_by_token(token):
        return Errors.ROOM_IS_NOT_EXISTS.value
    room = await db.get_room(token)
    return {'response': {'history': room.json()['history']}}