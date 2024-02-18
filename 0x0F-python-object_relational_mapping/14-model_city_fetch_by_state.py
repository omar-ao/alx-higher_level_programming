#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    usr, pwd, db = sys.argv[1:]
    url = "mysql://{}:{}@localhost:3306/{}".format(usr, pwd, db)

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State.name, City.id, City.name).join(City).all()
    for state in states:
        print('{}: ({}) {}'.format(state[0], state[1], state[2]))
