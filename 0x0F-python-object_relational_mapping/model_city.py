#!/usr/bin/python3
""" Cities in state
    file that contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    """Class City that inherits from Base

    Args:
        Base ([class]): class base
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
