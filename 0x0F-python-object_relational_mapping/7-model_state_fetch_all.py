#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                          argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    # session for query
    session = Session()
    # create the model
    Base.metadata.create_all(engine)
    # query the states for data
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{} {}".format(state.id, state.name))
    # close session
    session.close()
