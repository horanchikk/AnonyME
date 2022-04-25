from enum import Enum
from utils import gen_error


class Errors(Enum):
    """Errors class keeps all app errors with error codes"""
    USERNAME_IS_EXISTS = gen_error('this username is exists', 1)
    USER_IS_NOT_EXISTS = gen_error('this user is not exists', 2)
    ROOM_IS_NOT_EXISTS = gen_error('this room is not exists', 3)
    USER_HASNOT_ROOM = gen_error('this user has not the room', 4)
    TEXT_IS_EMPTY = gen_error('text is empty', 5)
    ROOM_IS_FULL = gen_error('room is full', 6)
