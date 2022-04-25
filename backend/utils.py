from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from fastapi import Response


async def gen_token(size: int = 64) -> str:
    """This function generates ASCII token"""
    return ''.join([
        choice(ascii_lowercase + ascii_uppercase + digits)
        for i in range(size)
    ])


async def gen_error(
        value: str,
        error_code: int
) -> Response:
    """This function generates an error response."""
    return Response(
        content=f'{{"detail": {{"message": "{value}", "code": {error_code}}}}}',
        status_code=400)
