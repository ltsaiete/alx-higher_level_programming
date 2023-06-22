#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from relationship_city import City

if __name__ == '__main__':
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        USER, PASS, DB), pool_pre_ping=True)
    engine.connect()

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()

    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
