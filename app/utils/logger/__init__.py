"""
Class Config Helper
@author Irfan Andriansyah <irfan@99.co>
"""
import os
import logging
import logging.handlers
from datetime import datetime

from app.abstract.logger import LoggerAbstract
from app.utils.config import ConfigHelper


class Logger(LoggerAbstract):
    """
    Logger
    """

    def __init__(self, config: ConfigHelper, date: datetime, filename: str):
        """
        Constructor
        :param config: ConfigHelper
        :param date: datetime
        """
        super(Logger, self).__init__(config, date, filename)
        self.set_logger()

    def set_logger(self):
        """
        Setter logger attribute
        """
        log_file = self.get_path_logger(self.filename)
        self.logger = logging.getLogger('{}__logger'.format(self.filename))

        handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=self.MAX_BYTES, backupCount=1
        )
        self.logger.addHandler(handler)

    def get_path_logger(self, filename: str) -> str:
        """
        Get current directory for logging path
        """
        path = self.config.get('path', 'logging_path')

        try:
            os.mkdir(path)
        except FileExistsError:
            pass

        return '{}{}.log'.format(path, filename)

    def send_to_logger(self, message: str, type_log: str):
        """
        to invoke function logger
        :param message: str
        :param type_log: str
        """
        self.logger.error(
            "{} [{}] {}".format(self.current_time(), type_log, message)
        )
        self.log(message, type_log)
