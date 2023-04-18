#!/usr/bin/python3
"""
This is a simple module and it only has
 the class definition of a City and
an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    This is the class definition of a City

    Args:
        id(int): city id
        name(str): city name

    Returns:
        void
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    state_id = Column()
