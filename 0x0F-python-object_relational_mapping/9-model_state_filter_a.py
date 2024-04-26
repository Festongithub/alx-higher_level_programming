#!/usr/bin/python3
"""
Script that prints the first State object from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    s_tate = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()

    for i in s_tate:
        print("{}: {}".format(i.id, i.name))
    session.close()
