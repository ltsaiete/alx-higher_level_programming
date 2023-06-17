#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_city import Base, City
from model_state import State
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

    cities = session.query(City, State.name).filter(
        City.state_id == State.id).order_by(City.id)
    for city, state in cities:
        print(f'{state}: ({city.id}) {city.name}')
