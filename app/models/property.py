"""
Property Model
@author Irfan Andriansyah <irfan@99.co>
"""

from sqlalchemy import Column, Text, BIGINT, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.models.localities import LocalitiesModel

BASE = declarative_base()


class PropertiesModel(BASE):
    """
    Properties Model
    """

    __tablename__ = 'Properties'
    id = Column(BIGINT, primary_key=True)
    title = Column(Text)
    locationId = Column(Integer)
    localityId = Column(Integer, ForeignKey(LocalitiesModel.id))
    isRemoved = Column(Integer)
    status = Column(Integer)
    localityMVId = Column(Integer)
    additionalRegion = Column(Text)
    address = Column(Text)
    locality = relationship(LocalitiesModel, backref='Properties')
