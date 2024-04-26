#!/usr/bin/python3
"""Python module to create the base model"""
import sqlalchemy
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
if __name__ == '__main__':
    """create engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                          argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    """session for query"""
    session = Session()
    """create the model"""
    Base.metadata.create_all(engine)
    """query the states for data"""
    cities = session.query(State, City).join(City).order_by(City.id)
    for state, city in cities:
        print("{} ({}) {}".format(state.name, city.id, state.name))
    """close session"""
    session.close()
