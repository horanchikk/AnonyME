# -*- coding: utf-8 -*-
"""Python anonyME client implementation"""
from typing import Dict, Any

from requests import Session


class AnonymeClient:
    def __init__(
            self,
            api_url: str = "http://localhost:8000/"
    ):
        self.session = Session()
        self.API_URL = api_url

    def users_get_all(
            self
    ) -> Dict[str, Any]:
        return self.session.get(
            f'{self.API_URL}users/getall'
        ).json()
