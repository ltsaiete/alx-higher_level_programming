#!/usr/bin/python3
"""
Write a script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    engine.connect()

    session = Session(bind=engine)

    states = session.query(State).order_by(State.id)

    for state in states:
        print(f'{state.id}: {state.name}')
