"""
Database Interface
@author Irfan Andriansyah <irfan@99.co>
"""
from abc import ABC
from typing import Any


class DatabaseConfigInterface(ABC):
    """
    Database Config Interface
    """
    username: str
    host: str
    port: str
    database: str
    password: str

    pass


class DatabaseQueryInterface(ABC):
    """
    Database Config Interface
    """
    connection: Any = None
    exec: Any = None

    pass


class DatabaseFactoryInterface(ABC):
    """
    Database Factory Interface
    """
    connection: DatabaseConfigInterface
    query: DatabaseQueryInterface

    pass
