#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        USER, PASS, DB), pool_pre_ping=True)
    engine.connect()

    session = Session(bind=engine)

    state = session.query(State).get(2)
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
