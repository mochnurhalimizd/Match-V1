"""
Localities Model
@author Irfan Andriansyah <irfan@99.co>
"""

from sqlalchemy import Column, Text, BIGINT
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class LocalitiesModel(BASE):
    """
    Localities Model
    """

    __tablename__ = 'Localities'
    id = Column(BIGINT, primary_key=True)
    country = Column(Text)
    province = Column(Text)
    locality = Column(Text)
    sublocality1 = Column(Text)
    sublocality2 = Column(Text)
    sublocality3 = Column(Text)
