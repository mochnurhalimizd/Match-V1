"""
Class HTTP Factory
@author Irfan Andriansyah <irfan@99.co>
"""

import sys

from app.modules.request import Request
from app.abstract.logger import LOGGER_TYPE
from app.utils.error import raise_
from app.utils.logger import Logger
from app.abstract.http import HttpRequestAbstract


class HttpFactory:
    """
    Database Factory
    """

    def __init__(self, type_lib: str, logger: Logger):
        """
        Constructor
        :param type_lib: str
        :param logger: Logger
        """
        self.type: str = type_lib
        self.logger: Logger = logger
        self.library: HttpRequestAbstract = self.set_library()

    def set_library(self) -> HttpRequestAbstract:
        """
        Generate library
        """
        try:
            return HttpFactory.get_option() \
                .get('library') \
                .get(
                    self.type, lambda: raise_(
                        ValueError('Invalid Option Type Library HTTP Request')
                    )
                )()
        except ValueError as e:
            import traceback
            traceback.print_exc()

            self.logger.send_to_logger(e, LOGGER_TYPE.get('ERROR'))
            sys.exit(1)

    @staticmethod
    def get_option():
        """
        Get option for type library
        """
        return {'library': {'request': Request}}
