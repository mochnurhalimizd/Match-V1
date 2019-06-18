"""
Class Config Helper
@author Irfan Andriansyah <irfan@99.co>
"""
import os
from configparser import ConfigParser


class ConfigHelper:
    """
    Config Helper Helper
    """

    config: ConfigParser

    def __init__(self, filename: str):
        """
        Constructor
        :param filename: str
        """
        self.set_config(filename)

    def set_config(self, filename: str):
        """
        initial config based on filename
        :param filename: str
        """
        try:
            self.config = ConfigParser()
            self.config.read(
                os.path.join(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__))
                            )
                        )
                    ), filename
                )
            )
        except Exception as err:
            raise Exception(err)

    def get(self, section: str, key: str) -> str:
        """
        Get object config based on key and section in config files
        :param section: str
        :param key: str
        """
        try:
            return self.config.get(section, key)
        except Exception as err:
            raise Exception(err)
