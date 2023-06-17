#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
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

    state = session.query(State).first()
    print(f'{state.id}: {state.name}')
