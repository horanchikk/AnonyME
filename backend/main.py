from fastapi import FastAPI
from utils import gen_token, gen_error
from database import Database


app = FastAPI()
db = Database()


@app.get('/create-user')
async def create_user(username: str):
    """This function creates a new user."""
    if await db.has_user(username):
        return await gen_error('this username is exists', 1)
    token = await gen_token()
    await db.add_user(username, token)
    return {
        'response': {
            'username': username,
            'token': token
        }
    }


@app.get('/create-room')
async def create_room(name: str):
    """This function creates a new room."""
    token = await gen_token()
    await db.add_room(name, token)
    return {
        'response': {
            'name': name,
            'token': token
        }
    }


@app.get('/get-user')
async def get_user(token: str):
    """This function returns user data"""
    if not await db.has_user_by_token(token):
        return await gen_error('this user is not exists', 2)
    user = await db.get_user(token)
    return {'response': user.json()}
