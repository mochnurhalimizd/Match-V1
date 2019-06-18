"""
MySQL Helper
@author Irfan Andriansyah <irfan@99.co>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Any

from app.abstract.database import \
    DatabaseConnectionAbstract, \
    DatabaseQueryAbstract


class MySQLDatabaseConnection(DatabaseConnectionAbstract):
    """
    Database Connection Helper
    """

    def get_connection_config(self):
        """
        Get connection string
        """
        return "mysql://{}:{}@{}:{}/{}".format(
            self.config.username, self.config.password, self.config.host,
            self.config.port, self.config.database
        )

    def set_connection(self):
        """
        Set connection & engine
        """
        self.engine = create_engine(self.get_connection_config(), echo=True)
        self.connection = self.engine.connect()
        self.session = sessionmaker(self.engine)()


class MySQLDatabaseQuery(DatabaseQueryAbstract):
    """
    Database Query Helper
    """

    def select(self, *args: Any):
        """
        Select query
        """
        self.exec = self.connection.session.query(*args)

        return self

    def update(self, *args: Any):
        """
        Select query
        """
        self.exec = self.connection.session.query(*args)

        return self

    def where(self, *args: str):
        """
        Add where clause
        """
        for arg in args:
            self.exec = self.exec.filter(arg)

        return self

    def join(self, model: Any):
        """
        Add join clause
        :param model: Any
        """
        self.exec = self.exec.join(model)

        return self

    def values(self, model: Any):
        """
        Add join clause
        :param model: Any
        """
        self.exec = self.exec.update(model)

        return self

    def limit(self, limit: int):
        """
        Add limit clause
        :param limit: int
        """
        self.exec = self.exec.limit(limit)

        return self

    def slice(self, start: int, stop: int):
        """
        Add limit offset clause
        :param start: int
        :param stop: int
        """
        self.exec = self.exec.slice(start, stop)

        return self

    def one(self):
        """
        Fetch one query
        """
        return self.exec.one()

    def first(self):
        """
        Fetch one query
        """
        return self.exec.first()

    def all(self):
        """
        Fetch all query
        """
        return self.exec.all()
