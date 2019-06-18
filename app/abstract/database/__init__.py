"""
Class Database Abstract
@author Irfan Andriansyah <irfan@99.co>
"""
from abc import ABC, abstractmethod
from typing import Any

from app.interface.database import \
    DatabaseConfigInterface, \
    DatabaseQueryInterface


class DatabaseConnectionAbstract(ABC):
    """
    Database Connection Abstract
    """

    engine: Any = None
    connection: Any = None
    session: Any = None

    def __init__(self, config: DatabaseConfigInterface):
        """
        Constructor
        :param config: DatabaseConfigInterface
        """
        self.config: DatabaseConfigInterface = config
        self.set_connection()

    @abstractmethod
    def set_connection(self):
        """
        Set database connection
        """
        pass


class DatabaseQueryAbstract(ABC):
    """
    Database Query Abstract
    """

    def __init__(self, config: DatabaseQueryInterface):
        """
        Constructor
        :param config: DatabaseQueryInterface
        """
        self.exec: Any = None
        self.connection: DatabaseConnectionAbstract = config.connection

    @abstractmethod
    def select(self, *args: Any):
        """
        Select query
        :param *args: Any Database Model
        """
        pass

    @abstractmethod
    def where(self, *args: str):
        """
        Add where clause
        """
        pass
    
    @abstractmethod
    def update(self, *args: str):
        """
        Add where clause
        """
        pass

    @abstractmethod
    def join(self, model: Any):
        """
        Add join clause
        :param model: Any
        """
        pass

    @abstractmethod
    def limit(self, limit: int):
        """
        Add limit clause
        :param limit: int
        """
        pass

    @abstractmethod
    def slice(self, start: int, stop: int):
        """
        Add limit offset clause
        :param start: int
        :param stop: int
        """
        pass

    @abstractmethod
    def one(self):
        """
        Fetch one query
        """
        pass

    @abstractmethod
    def all(self):
        """
        Fetch all query
        """
        pass
