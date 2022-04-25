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
                users text not null,
                users_limit int not null
            );'''
        )
        self.connection.commit()
    
    async def add_room(
            self,
            name: str,
            token: str,
            users_limit: int
    ) -> NoReturn:
        """Adds a new room in database."""
        self.cursor.execute(
            'insert into room (name, token, history, users, users_limit) values (?, ?, ?, ?, ?)',
            (name, token, '[]', '[]', users_limit)
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
        """Returns user data as User class"""
        result = self.cursor.execute(
            'select * from user where token = ?', (token,)
        ).fetchone()
        return User(result)
    
    async def get_users(self) -> User:
        """Returns user data as Users class"""
        result = self.cursor.execute('select * from user').fetchall()
        return [User(i) for i in result]
    
    async def get_room(
            self,
            token: str
    ) -> Room:
        """Returns room data as Room class"""
        result = self.cursor.execute(
            'select * from room where token = ?', (token,)
        ).fetchone()
        return Room(result)
    
    async def get_rooms(self) -> Room:
        """Returns room data as Rooms class"""
        result = self.cursor.execute('select * from room').fetchall()
        return [Room(i) for i in result]
    
    async def has_room_by_token(
            self,
            token: str
    ) -> bool:
        """Returns True when room with token is exists."""
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
        """Returns True when user with token is exists."""
        return bool(
            self.cursor.execute(
                'select * from user where token = ?', (token,)
            ).fetchone()
        )
    
    async def remove_room(
            self,
            token: str
    ) -> NoReturn:
        """Removes the room object"""
        self.cursor.execute(
            'delete from room where token = ?', (token,)
        )
        self.connection.commit()
    
    async def remove_user(
            self,
            token: str
    ) -> NoReturn:
        """Removes the user object"""
        self.cursor.execute(
            'delete from user where token = ?', (token,)
        )
        self.connection.commit()
    
    async def save_room(
            self,
            room: Room
    ) -> NoReturn:
        """Saves Room object"""
        self.cursor.execute(
            'update room set (name, history, users, users_limit) = (?, ?, ?, ?) where id = ?',
            (room.name, dumps(room.history), dumps(room.users), room._id, room.users_limit)
        )
        self.connection.commit()
    
    async def save_user(
            self,
            user: User
    ) -> NoReturn:
        """Saves User object"""
        self.cursor.execute(
            'update user set (username, room) = (?, ?) where id = ?',
            (user.username, user.room, user._id)
        )
        self.connection.commit()
