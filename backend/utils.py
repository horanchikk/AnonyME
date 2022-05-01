from random import choice
from string import ascii_lowercase, ascii_uppercase, digits

from fastapi import status
from fastapi.responses import JSONResponse


async def gen_token(size: int = 64) -> str:
    """This function generates ASCII token"""
    return ''.join([
        choice(ascii_lowercase + ascii_uppercase + digits)
        for i in range(size)
    ])


def gen_error(
        value: str,
        error_code: int
) -> JSONResponse:
    """This function generates an error response."""
    return JSONResponse(
        content={
            'detail': {
                'message': value,
                'code': error_code
            }
        }, status_code=status.HTTP_400_BAD_REQUEST
    )
