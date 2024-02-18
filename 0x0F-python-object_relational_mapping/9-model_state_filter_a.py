#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    usr, pwd, db = sys.argv[1:]
    url = "mysql://{}:{}@localhost:3306/{}".format(usr, pwd, db)

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")).order_by()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
