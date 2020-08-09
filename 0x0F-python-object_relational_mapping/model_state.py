#!/usr/bin/python3
""" First state model
    file that contains the class definition of a State
    and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class State that inherits from Base

    Args:
        Base ([class]): class base
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
