# -*- coding: utf-8 -*-
from typing import Optional, Dict, Any


class AnonymeException(Exception):
    """Base anonyme exception"""
    def __init__(
            self,
            msg: str,
            code: int
    ):
        self.msg = msg
        self.code = code


def handle_error(
        response: Dict[str, Any]
) -> Optional[AnonymeException]:
    """Handles errors in response

    :param response: AnonyME response"""
    if 'detail' in response:
        code = response['detail']['code']
        msg = response['detail']['message']
        return AnonymeException(msg, code)
    return None
