from fastapi import FastAPI, WebSocketDisconnect, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from utils import gen_token, gen_error
from database import Database
from message import Message
from websocket_manager import WebsocketManager


manager = WebsocketManager()
app = FastAPI()
db = Database()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/user/new')
async def create_user(name: str):
    """This function creates a new user."""
    if await db.has_user(name):
        return await gen_error('this username is exists', 1)
    token = await gen_token()
    await db.add_user(name, token)
    return {
        'response': {
            'username': name,
            'token': token
        }
    }


@app.get('/user/get')
async def get_user(token: str):
    """This function returns user data"""
    if not await db.has_user_by_token(token):
        return await gen_error('this user is not exists', 2)
    user = await db.get_user(token)
    return {'response': user.json()}


@app.get('/user/getall')
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


@app.get('/user/messages.send')
async def user_send_message(text: str, token: str):
    """Sends message to the room"""
    if not await db.has_user_by_token(token):
        return await gen_error('this user is not exists', 2)
    if not text:
        return await gen_error('text is empty', 4)
    user = await db.get_user(token)
    if not user.room:
        return await gen_error('this user has not the room', 3)
    room = await db.get_room(user.room)
    message = Message(text, user.username)
    room.add_msg(message)
    await db.save_room(room)
    await manager.broadcast_to_room(
        {'response': message.json()},
        db, room.token
    )
    return {'response': 'success'}


@app.websocket("/user/poll")
async def websocket_endpoint(websocket: WebSocket, token: str):
    if not await db.has_user_by_token(token):
        return
    user = await db.get_user(token)
    if not user.room:
        return
    await manager.connect(websocket, user.token, user.room)
    try:
        while True:
            text = await websocket.receive_text()
            message = Message(text, user.username)
            room = await db.get_room(user.room)
            room.add_msg(message)
            await manager.send_personal(websocket, {'response': 'success'})
            await manager.broadcast_to_room(
                {'response': message.json()},
                db, room.token
            )
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast_to_room({
            'response': Message(
                f'{user.username} left the chat',
                user.username, 'left from chat', 2).json()}, db, user.token)


@app.get('/user/room.enter')
async def enter_in_room(token: str, room_token: str):
    """Changes current user's room"""
    if not await db.has_user_by_token(token):
        return await gen_error('this user is not exists', 2)
    if not await db.has_room_by_token(room_token):
        return await gen_error('this room is not exists', 2)
    user = await db.get_user(token)
    if user.room:
        await manager.broadcast_to_room({
            'response': Message(
                f'{user.username} left from chat',
                user.username, 'left from chat', 2
            ).json()}, db, room_token)
        room = await db.get_room(user.room)
        room.users.remove(user._id)
        await db.save_room(room)
    await manager.broadcast_to_room({
        'response': Message(
            f'{user.username} join the chat',
            user.username, 'join the chat', 3
        ).json()}, db, room_token)
    room = await db.get_room(room_token)
    room.add_user(user._id)
    user.room = room_token
    await db.save_room(room)
    await db.save_user(user)
    return {'response': 'success'}


@app.get('/room/new')
async def create_room(name: str, user_token: str):
    """This function creates a new room."""
    if not await db.has_user_by_token(user_token):
        return await gen_error('this user is not exists', 2)
    token = await gen_token()
    await db.add_room(name, token)

    user = await db.get_user(user_token)
    room = await db.get_room(token)
    room.add_user(user._id)
    user.room = token
    await db.save_room(room)
    await db.save_user(user)
    return {
        'response': {
            'name': name,
            'token': token
        }
    }


@app.get('/room/get')
async def get_room(token: str):
    """This function returns room data"""
    if not await db.has_room_by_token(token):
        return await gen_error('this room is not exists', 2)
    room = await db.get_room(token)
    return {'response': room.json()}


@app.get('/room/getall')
async def get_all_rooms():
    """This returns all rooms"""
    rooms = await db.get_rooms()
    return {
        'response': [{
            'id': i._id,
            'name': i.name,
            'token': i.token
        } for i in rooms]
    }


@app.get('/room/history.get')
async def get_room_history(token: str):
    """Returns room messages history"""
    if not await db.has_room_by_token(token):
        return await gen_error('this room is not exists', 2)
    room = await db.get_room(token)
    return {'response': {'history': room.json()['history']}}


# user Ethosa boAIgLTDdql23fD1g6jBv15TZPFg9JztshpxmEKCp0135lasTDtaT6TO2Na8glzd
# user ктоЯ xuRxe9XTz7brXy9IhgpU0DXOvaJ4sM7abag401DUssWxXVRSKeQRJEoUaI3048XH
# room Ethosa room 5VWkW7al937eqUJ6CwRVyV8roSMQTgxHCeEIqG8KEjQBpvO4GNGT66ZrXrOxRj3P
# room ASD c81l5uNJs5LJp5eY1gm7maMe085Z0p3pSQa6xQcSgqx83w0w7lA6vIeOsvPLpmcI
