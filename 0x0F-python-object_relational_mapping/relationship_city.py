#!/usr/bin/python3
"""Defines class City that inherits from Base"""


from sqlalchemy import (Integer, String, Column, ForeignKey)
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """Defines class City that defines sql table cities

    attributes:
        id (integer): talbe id
        name (string): table name
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
