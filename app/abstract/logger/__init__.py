"""
Class Logger Abstract
@author Irfan Andriansyah <irfan@99.co>
"""
from abc import ABC, abstractmethod
from typing import Dict
from datetime import datetime

from app.utils.config import ConfigHelper

LOGGER_TYPE: Dict[str, str] = {
    "ERROR": "ERROR",
    "INFO": "INFO",
    "WARNING": "WARNING"
}


class LoggerAbstract(ABC):
    """
    Logger Abstract
    """

    MAX_BYTES: int = 10485760
    logger = None

    def __init__(self, config: ConfigHelper, date: datetime, filename: str):
        """
        Constructor
        :param config: ConfigHelper
        :param date: datetime
        """
        self.config = config
        self.datetime = date
        self.filename = filename

    @abstractmethod
    def set_logger(self):
        """
        Setter logger attribute
        """
        pass

    @abstractmethod
    def send_to_logger(self, message: str, type_log: str):
        """
        to invoke function logger
        :param message: str
        :param type_log: str
        """
        pass

    def current_time(self) -> str:
        """
        Get current time
        """
        return self.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, message: str, type_log: str):
        """
        to print log
        :param message: str
        :param type_log: str
        """
        print("{0} [{1}] {2}".format(self.current_time(), type_log, message))
