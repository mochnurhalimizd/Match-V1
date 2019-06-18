"""
Class HttpRequest Abstract
@author Irfan Andriansyah <irfan@99.co>
"""
import requests
from typing import Any, Dict
from app.abstract.http import HttpRequestAbstract


class Request(HttpRequestAbstract):
    """
    Request http library
    """

    def __init__(self):
        """
        Constructor
        """
        super(Request, self).__init__()
        self.exec: Any = None

    def get(
        self,
        url: str,
        params: Dict[str, Any] = None,
        headers: Dict[str, Any] = None
    ) -> HttpRequestAbstract:
        """
        Access HTTP Request Via Method GET
        """
        self.exec = requests.get(url, params=params, headers=headers)

        return self

    def url(self) -> str:
        """
        Get Url API
        """
        return self.exec.url

    def json(self) -> Any:
        """
        Get Response Http (Convert to dictionary / list)
        """
        return self.exec.json()

    def text(self) -> str:
        """
        Get Response Http (Convert to json string)
        """
        return self.exec.text

    def status_code(self) -> int:
        """
        Get Status Code Http Request
        """
        return self.exec.status_code

    def headers(self, key: str) -> int:
        """
        Get Headers Key Value From Http Request
        """
        return self.exec.headers.get(key, 'Oops headers is not found')
