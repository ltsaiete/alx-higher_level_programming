#!/usr/bin/python3
"""
script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    USER = sys.argv[1]
    PASS = '' #sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        USER, PASS, DB), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)

    session.add(state)
    session.commit()
