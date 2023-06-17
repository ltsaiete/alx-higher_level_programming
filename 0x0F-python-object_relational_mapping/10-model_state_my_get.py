#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
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

    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state:
        print(state.id)
    else:
        print('Not found')
