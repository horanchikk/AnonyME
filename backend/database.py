from sqlite3 import connect
from json import loads, dumps
from typing import NoReturn, Dict, Any
from user import User
from room import Room


class Database:
    def __init__(
            self,
            filename: str = 'database.db'
    ) -> None:
        self.connection = connect(filename)
        self.cursor = self.connection.cursor()

        # rooms is array of rooms IDs
        self.cursor.execute(
            '''create table if not exists user(
                id integer primary key,
                username text not null,
                token text not null,
                room text not null
            );'''
        )
        # users is array of users IDs
        # history is array of messages
        self.cursor.execute(
            '''create table if not exists room(
                id integer primary key,
                name text not null,
                token text not null,
                history text not null,
                users text not null
            );'''
        )
        self.connection.commit()
    
    async def add_room(
            self,
            name: str,
            token: str
    ) -> NoReturn:
        """Adds a new room in database."""
        self.cursor.execute(
            'insert into user (name, token, history, users) values (?, ?, ?, ?)',
            (name, token, '[]', '[]')
        )
        self.connection.commit()
    
    async def add_user(
            self,
            username: str,
            token: str
    ) -> NoReturn:
        """Adds a new user in database."""
        self.cursor.execute(
            'insert into user (username, token, room) values (?, ?, ?)',
            (username, token, '')
        )
        self.connection.commit()
    
    async def get_user(
            self,
            token: str
    ) -> User:
        result = self.cursor.execute(
            'select * from user where token = ?', (token,)
        ).fetchone()
        return User(result)
    
    async def has_room_by_token(
            self,
            token: str
    ) -> bool:
        return bool(
            self.cursor.execute(
                'select * from room where token = ?', (token,)
            ).fetchone()
        )
    
    async def has_user(
            self,
            username: str
    ) -> bool:
        return bool(
            self.cursor.execute(
                'select * from user where username = ?', (username,)
            ).fetchone()
        )
    
    async def has_user_by_token(
            self,
            token: str
    ) -> bool:
        return bool(
            self.cursor.execute(
                'select * from user where token = ?', (token,)
            ).fetchone()
        )
    
    async def save_room(
            self,
            room: Room
    ) -> NoReturn:
        self.cursor.execute(
            'update table room (name, history, users) values (?, ?, ?) where id = ?',
            (room.name, dumps(room.history), dumps(room.users), room._id)
        )
    
    async def save_user(
            self,
            user: User
    ) -> NoReturn:
        self.cursor.execute(
            'update table user (username, room) values (?, ?) where id = ?',
            (user.username, user.room, user._id)
        )
