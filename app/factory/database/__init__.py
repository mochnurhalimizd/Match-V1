"""
Class Database Factory
@author Irfan Andriansyah <irfan@99.co>
"""
import sys
from typing import Any

from app.utils.config import ConfigHelper
from app.abstract.logger import LOGGER_TYPE
from app.interface.database import \
    DatabaseFactoryInterface, \
    DatabaseConfigInterface, \
    DatabaseQueryInterface
from app.utils.logger import Logger
from app.utils.error import raise_
from app.modules.mysql import MySQLDatabaseConnection, MySQLDatabaseQuery


class DatabaseFactory:
    """
    Database Factory
    """

    def __init__(self, type_db: str, config: ConfigHelper, logger: Logger):
        """
        Constructor
        :param type_db: str
        :param config: ConfigHelper
        :param logger: Logger
        """
        self.type: str = type_db
        self.config: ConfigHelper = config
        self.logger: Logger = logger

        db: DatabaseFactoryInterface = self.set_db()
        self.query: DatabaseQueryInterface = db.query
        self.connection: DatabaseConfigInterface = db.connection

    def set_db(self) -> DatabaseFactoryInterface:
        """
        Generate database factory
        """
        try:
            factory = DatabaseFactoryInterface()
            factory.connection = self.get_option() \
                .get('connection') \
                .get(
                    self.type, lambda: raise_(
                        ValueError('Invalid Option Type Connection Database')
                    )
                )()
            factory.query = self.get_option() \
                .get('query') \
                .get(
                    self.type, lambda: raise_(
                        ValueError('Invalid Option Type Query Database')
                    )
                )(factory.connection)

            return factory
        except ValueError as e:
            import traceback
            traceback.print_exc()

            self.logger.send_to_logger(e, LOGGER_TYPE.get('ERROR'))
            sys.exit(1)

    def get_option(self):
        """
        Get option for type database
        """
        return {
            'connection': {
                'MySQL':
                lambda: MySQLDatabaseConnection(self.get_config_connection())
            },
            'query': {
                'MySQL':
                lambda connection: MySQLDatabaseQuery(
                    DatabaseFactory.get_config_query(connection)
                )
            }
        }

    @staticmethod
    def get_config_query(connection: Any) -> DatabaseQueryInterface:
        """
        Generate config for query database factory
        """
        config = DatabaseQueryInterface()
        config.connection = connection

        return config

    def get_config_connection(self) -> DatabaseConfigInterface:
        """
        Generate config for connection database factory
        """
        config = DatabaseConfigInterface()
        config.database = self.config.get('database', 'database')
        config.host = self.config.get('database', 'host')
        config.password = self.config.get('database', 'password')
        config.port = self.config.get('database', 'port')
        config.username = self.config.get('database', 'username')

        return config
