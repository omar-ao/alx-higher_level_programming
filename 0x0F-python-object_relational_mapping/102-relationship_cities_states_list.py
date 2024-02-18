#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    usr, pwd, db = sys.argv[1:]
    url = "mysql://{}:{}@localhost:3306/{}".format(usr, pwd, db)

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.cities.name))
