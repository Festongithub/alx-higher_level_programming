#!/usr/bin/python3
# creates a model of the state
import sqlalchemy
from sqlalchemy import Column, String, MetaData, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# class state


class State(Base):
    # class attributes
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
