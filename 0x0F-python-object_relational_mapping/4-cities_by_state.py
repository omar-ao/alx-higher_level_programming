#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa

Usage:
    ./4-cities_by_state.py <user> <password> <db>
"""

import MySQLdb
import sys


if __name__ == '__main__':
    host, port = 'localhost', 3306
    usr, pwd, db = sys.argv[1:]

    conn = MySQLdb.connect(host=host, port=port, user=usr, passwd=pwd, db=db)
    cur = conn.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "INNER JOIN states ON cities.state_id=states.id "
             "ORDER BY cities.id")
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
