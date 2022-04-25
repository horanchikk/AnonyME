from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


def gen_token(size: int = 64) -> str:
    return ''.join([
        choice(ascii_lowercase + ascii_uppercase + digits)
        for i in range(size)
    ])
