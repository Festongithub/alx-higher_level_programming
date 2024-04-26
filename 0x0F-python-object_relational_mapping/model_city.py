#!/usr/bin/python3

""" creates a state model for the base"""
from sqlalchemy import Column, String,  Integer, ForeignKey
from model_state import Base

class City(Base):
    """
    class attributes
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
