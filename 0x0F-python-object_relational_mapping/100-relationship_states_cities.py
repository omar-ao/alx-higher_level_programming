#!/usr/bin/python3
"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
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

    usr, pwd, db, = sys.argv[1:]
    url = "mysql://{}:{}@localhost:3306/{}".format(usr, pwd, db)

    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    st = State(name='California')
    city = City(name='San Francisco')
    st.cities.append(city)

    session.add(st)
    session.commit()
    session.close()
