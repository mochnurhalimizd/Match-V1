"""
Class HttpRequest Abstract
@author Irfan Andriansyah <irfan@99.co>
"""
from abc import ABC, abstractmethod
from typing import Any, Dict


class HttpRequestAbstract(ABC):
    """
     HttpRequest Abstract
    """

    def __init__(self):
        """
        Constructor
        """
        self.exec: Any = None

    @abstractmethod
    def get(
        self,
        url: str,
        params: Dict[str, Any] = None,
        headers: Dict[str, Any] = None
    ) -> 'HttpRequestAbstract':
        """
        Access HTTP Request Via Method GET
        """
        pass

    @abstractmethod
    def json(self) -> Any:
        """
        Get Response Http (Convert to dictionary / list)
        """
        pass

    @abstractmethod
    def url(self) -> str:
        """
        Get Url API
        """
        pass

    @abstractmethod
    def text(self) -> str:
        """
        Get Response Http (Convert to json string)
        """
        pass

    @abstractmethod
    def status_code(self) -> int:
        """
        Get Status Code Http Request
        """
        pass

    @abstractmethod
    def headers(self, key: str) -> int:
        """
        Get Headers Key Value From Http Request
        """
        pass
