# -*- coding: utf-8 -*-
"""Python anonyME client implementation"""
from typing import Dict, Any

from requests import Session
from .exceptions import handle_error


class AnonymeClient:
    def __init__(
            self,
            api_url: str = "http://localhost:8000/"
    ):
        """Initializes AnonyME client

        :param api_url: AnonyME API url"""
        self.session = Session()
        self.API_URL = api_url

    def _send_req(
            self,
            url: str
    ) -> Dict[str, Any]:
        """Sends request to AnonyME API.

        :param url: request URL."""
        res = self.session.get(url).json()
        error = handle_error(res)
        if error:
            raise error
        return res

    def users_get(
            self,
            token: str
    ) -> Dict[str, Any]:
        """Returns user by his token

        :param token: user's token.

        :raises AnonymeException: user isn't exists
        """
        return self._send_req(
            f'{self.API_URL}users/get?token={token}'
        )

    def users_get_all(
            self
    ) -> Dict[str, Any]:
        """Returns all active users"""
        return self._send_req(
            f'{self.API_URL}users/getall'
        )

    def users_new(
            self,
            name: str
    ) -> Dict[str, Any]:
        """Creates new user with name

        :param name: user's name

        :raises AnonymeException: username is exists"""
        return self._send_req(
            f'{self.API_URL}users/new?name={name}'
        )

    def users_remove(
            self,
            token: str
    ) -> Dict[str, Any]:
        """Removes user by token

        :param token: user's token

        :raises AnonymeException: user isn't exists"""
        return self._send_req(
            f'{self.API_URL}users/remove?token={token}'
        )

    def users_messages_send(
            self,
            token: str,
            text: str,
            sticker_id: int
    ) -> Dict[str, Any]:
        """Sends message to room by user's token.

        :param token: user's token
        :param text: message text
        :param sticker_id: sticker ID

        :raises AnonymeException: user isn't exists; message text is empty; user hasn't room"""
        return self._send_req(
            f'{self.API_URL}users/messages.send?token={token}&text={text}&sticker_id={sticker_id}'
        )

    def users_room_enter(
            self,
            token: str,
            room_token: str
    ) -> Dict[str, Any]:
        """Enter in room by token

        :param token: user's token
        :param room_token: room's token

        :raises AnonymeException: user or room isn't exists; room is full"""
        return self._send_req(
            f'{self.API_URL}users/room.enter?token={token}&room_token={room_token}'
        )

    def users_room_leave(
            self,
            token: str
    ) -> Dict[str, Any]:
        """Leave from room by user's token

        :param token: user's token

        :raises AnonymeException: user or room isn't exists; room is full"""
        return self._send_req(
            f'{self.API_URL}users/room.leave?token={token}'
        )

    def rooms_get_all(
            self
    ) -> Dict[str, Any]:
        """Returns all rooms"""
        return self._send_req(
            f'{self.API_URL}rooms/getall'
        )

    def rooms_get(
            self,
            token: str
    ) -> Dict[str, Any]:
        """Returns room by token

        :param token: room's token

        :raises AnonymeException: room isn't exists"""
        return self._send_req(
            f'{self.API_URL}rooms/get?token={token}'
        )

    def rooms_new(
            self,
            name: str,
            user_token: str,
            users_limit: int
    ) -> Dict[str, Any]:
        """Creates a new room by user's token

        :param name: room's name
        :param user_token: user's token
        :param users_limit: room users limit

        :raises AnonymeException: user isn't exists"""
        return self._send_req(
            f'{self.API_URL}rooms/new?name={name}&user_token={user_token}&users_limit={users_limit}'
        )
