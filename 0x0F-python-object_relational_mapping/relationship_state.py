#!/usr/bin/python3
"""
This is a simple module and it only has
one function called the class definition of a State and
an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    This is the class definition of a State

    Args:
        arg_1(type): description

    Returns:
        void
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref="state")
