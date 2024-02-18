#!/usr/bin/python3
"""Defines class State that inherits from Base"""


from sqlalchemy import (Integer, String, Column)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
