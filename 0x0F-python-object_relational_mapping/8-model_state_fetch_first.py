#!/usr/bin/python3
"""
8-model_state_fetch_first.py
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

    state = session.query(State).first()
    print('{}: {}'.format(state.id, state.name))
