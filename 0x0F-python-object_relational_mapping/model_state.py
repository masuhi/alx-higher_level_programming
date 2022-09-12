#!/usr/bin/python3
"""
Write a python file that contains the class definition
of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class definition of a State inherits from Base,
        links to the MySQL table states
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
