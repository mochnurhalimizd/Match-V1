"""
Cleansing Module
Module for cleansing and standarization locality from google API

@author Moch Nurhalimi Zaini D <moch.nurhalimi@gmai.com>
"""

import re

class Cleansing:
    """
    Cleansing and standarization Module
    """

    def replace_locality(self, text, dic):
        """
        Replace locality from google api
        :param text: string
        :param dict: dictionary
        """
        try : 
            for i, j in dic.items():
                text = text.lower().replace(i, j)
            return re.sub(' +', ' ',text.lstrip().rstrip().strip())
        except:
            return text
    
    def lower_locality(self, text):
        """
        Replace locality from google api
        :param text: string
        """
        try:
            return text.lower()
        except:
            return text
