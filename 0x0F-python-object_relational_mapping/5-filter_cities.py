#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa

Usage:
    ./5-filter_cities.py <user> <password> <db> <state name>
"""

import MySQLdb
import sys


if __name__ == "__main__":
    usr, pwd, db, state = sys.argv[1:]
    host, port = ('localhost', 3306)

    conn = MySQLdb.connect(host=host, user=usr, passwd=pwd, db=db)
    cur = conn.cursor()

    query = ("SELECT cities.name "
             "FROM cities "
             "INNER JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ")
    cur.execute(query, (state,))
    cities = cur.fetchall()
    cities = [city for tuple_ in cities for city in tuple_]
    print(", ".join(cities))
