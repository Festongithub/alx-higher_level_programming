#!/usr/bin/python3
"""
Class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey, text
from relationship_state import Base


class City(Base):
    """
    City class that inherits from Base

    Attributes:
        id: Id city
        name: Name of the city
        state_id: State id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
